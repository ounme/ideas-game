from __future__ import annotations
import random
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List, Any
from typing import Dict, List, Any

# Copyright (c) 2024 Никита Панин
# Dedicated to the glory of God
# Licensed under MIT License


@dataclass
class Idea:
    core: str
    effects: Dict[str, float]  # Изменения параметров: {'O': +5, 'C': -3, ...}
    complexity: float  # 0–100, влияет на искажение
    emotion: str  # Эмоциональный оттенок
    weight: float = 1.0  # «Сила» идеи в популяции

class Agent:
    def __init__(self, id: int):
        self.id = id
        # Параметры OCEAN + интеллект (0–100)
        self.O = random.uniform(30, 70)  # Открытость
        self.C = random.uniform(30, 70)  # Добросовестность
        self.E = random.uniform(30, 70)  # Экстраверсия
        self.A = random.uniform(30, 70)  # Доброжелательность
        self.N = random.uniform(20, 60)  # Нейротизм
        self.I = random.uniform(10, 80)  # Интеллект
        self.beliefs: List[Idea] = []  # Принятые идеи
        self.social_weight = self.calculate_social_weight()

    def calculate_social_weight(self) -> float:
        """Расчёт влияния агента на общину"""
        return (
            self.E * 0.4 +  # Экстраверсия (активность)
            self.C * 0.3 +  # Добросовестность (надёжность)
            self.I * 0.3    # Интеллект (авторитет)
        )

    def transmit_idea(self, idea: "Idea", recipient: "Agent", community: "List[Agent]"):
        """Передача идеи от источника к получателю"""
        # 1. Базовое искажение (зависит от сложности идеи)
        distortion = random.uniform(-0.1, 0.1) * (idea.complexity / 100)

        # 2. Корректировка искажения
        distortion *= (1 - self.I / 100)  # Интеллект источника снижает искажение
        distortion *= (1 + recipient.N / 100)  # Нейротизм получателя усиливает искажение

        # 3. Адаптация идеи под стиль источника
        modified_idea = self.adapt_idea(idea, recipient)

        # 4. Передача и применение
        recipient.receive_idea(modified_idea, distortion, community)

        # 5. Эволюция идеи после передачи
        self.evolve_idea(modified_idea, community)

    def adapt_idea(self, idea: "Idea", recipient: "Agent") -> "Idea":
        """Адаптация идеи под личность источника и получателя"""
        new_idea = Idea(
            core=idea.core,
            effects=idea.effects.copy(),
            complexity=idea.complexity,
            emotion=idea.emotion,
            weight=idea.weight
        )

        # Модификации в зависимости от параметров
        if self.A > 70:  # Высокий A → смягчение формулировок
            new_idea.core = f"Поразмышляй о {new_idea.core}"
        if self.C > 70:  # Высокий C → добавление правил
            new_idea.effects['C'] = new_idea.effects.get('C', 0) + 2
        if recipient.O < 40:  # Низкий O у получателя → упрощение
            new_idea.complexity *= 0.8
        if recipient.N > 70:  # Высокий N у получателя → усиление эмоций
            new_idea.emotion = f"страшный {new_idea.emotion}"

        return new_idea

    def receive_idea(self, idea: "Idea", distortion: float, community: "List[Agent]"):
        """Получение и применение идеи"""
        # Применение эффектов с фильтрами
        for param, delta in idea.effects.items():
            if hasattr(self, param):
                # Фильтр добросовестности: сопротивление негативным изменениям
                if param == 'C' and self.C > 80 and delta < 0:
                    delta *= 0.3
                # Фильтр нейротизма: усиление эмоциональных эффектов
                if param in ['N', 'A'] and self.N > 70:
                    delta *= 1.5
                # Применение с учётом искажения
                new_val = getattr(self, param) + delta * (1 - distortion)
                setattr(self, param, max(0.0, min(100.0, new_val)))

        # Добавление идеи в убеждения
        if idea not in self.beliefs:
            self.beliefs.append(idea)

        # Обновление социального веса
        self.social_weight = self.calculate_social_weight()

    def evolve_idea(self, idea: "Idea", community: "List[Agent]"):
        """Эволюция идеи после передачи"""
        # Рост веса при принятии многими
        idea.weight *= 1.01

        # Изменение сложности
        if self.O > 70:
            idea.complexity *= 1.05  # Усложнение
        else:
            idea.complexity *= 0.95  # Упрощение


        # Смена эмоционального оттенка
        if self.N > 80:
            idea.emotion = f"!тревожный {idea.emotion}"


class Community:
    def __init__(self, size: int = 20):
        self.agents: List[Agent] = [Agent(i) for i in range(size)]
        self.ideas: List[Idea] = []
        self.history: Dict[str, List[float]] = {
            'avg_O': [], 'avg_C': [], 'avg_E': [],
            'avg_A': [], 'avg_N': [], 'avg_I': []
        }

    def add_idea(self, idea: Idea):
        """Добавить идею в общину"""
        self.ideas.append(idea)

    def step(self):
        """Один шаг симуляции"""
        # Случайный выбор источника идеи
        source = random.choice(self.agents)
        if not self.ideas:
            return

        idea = random.choice(self.ideas)

        # Формирование списка получателей (все агенты, кроме источника)
        possible_recipients = [agent for agent in self.agents if agent != source]

        
        # Расчёт весов для возможных получателей
        weights = [
            source.E * (1 + agent.A / 100)  # Влияние экстраверсии источника и доброжелательности получателя
            for agent in possible_recipients
        ]

        # Выбор получателя с учётом весов
        recipient = random.choices(possible_recipients, weights=weights, k=1)[0]

        # Передача идеи
        source.transmit_idea(idea, recipient, self.agents)

        # Обновление истории
        self.update_history()


    def update_history(self):
        """Записать средние значения параметров"""
        for param in ['O', 'C', 'E', 'A', 'N', 'I']:
            avg = sum(getattr(agent, param) for agent in self.agents) / len(self.agents)
            self.history[f'avg_{param}'].append(avg)

    def plot_history(self):
        """Построить графики динамики"""
        plt.figure(figsize=(12, 6))
        for param in ['O', 'C', 'E', 'A', 'N', 'I']:
            plt.plot(self.history[f'avg_{param}'], label=f'Средний {param}')
        plt.xlabel('Шаги симуляции')
        plt.ylabel('Значение (0–100)')
        plt.title('Динамика параметров общины')
        plt.legend()
        plt.grid(True)
        plt.show()
# === ЗАПУСК СИМУЛЯЦИИ ===
if __name__ == "__main__":
    # Создание общины
    community = Community(size=30)

    # Добавление начальных идей
    community.add_idea(Idea(
        core="Соблюдай завет",
        effects={'C': +8, 'A': +5, 'N': -3},
        complexity=60,
        emotion="благоговение"
    ))
    
    community.add_idea(Idea(  # Исправлено: закрыт словарь effects и добавлен emotion
        core="Мсти врагам",
        effects={'E': +10, 'N': +7, 'A': -6},
        complexity=70,
        emotion="гнев"
    ))
    
    community.add_idea(Idea(
        core="Ищи знание",
        effects={'O': +12, 'I': +8, 'N': +4},
        complexity=80,
        emotion="любопытство"
    ))

    # Запуск симуляции
    print("Запуск симуляции распространения идей...")
    num_steps = 100
    for step in range(num_steps):
        community.step()
        if step % 20 == 0:
            print(f"Шаг {step}: средний O={community.history['avg_O'][-1]:.1f}, "
                  f"C={community.history['avg_C'][-1]:.1f}, "
                  f"E={community.history['avg_E'][-1]:.1f}")

    print(f"Симуляция завершена ({num_steps} шагов).")

    # Визуализация результатов
    community.plot_history()

    # Анализ финального состояния
    print("\n=== ИТОГИ СИМУЛЯЦИИ ===")
    final_stats = {}
    for param in ['O', 'C', 'E', 'A', 'N', 'I']:
        values = [getattr(agent, param) for agent in community.agents]
        final_stats[param] = {
            'mean': sum(values) / len(values),
            'min': min(values),
            'max': max(values),
            'std': (sum((x - final_stats[param]['mean'])**2 for x in values) / len(values))**0.5
        }
        print(f"{param}: среднее={final_stats[param]['mean']:5.1f} "
              f"(min={final_stats[param]['min']:4.1f}, max={final_stats[param]['max']:4.1f})")

    # Анализ распространения идей
    print("\n=== РАСПРОСТРАНЕНИЕ ИДЕЙ ===")
    for idea in community.ideas:
        adopters = sum(1 for agent in community.agents if idea in agent.beliefs)
        print(f"'{idea.core}': принята {adopters}/{len(community.agents)} агентами "
              f"(вес={idea.weight:.2f}, сложность={idea.complexity:.1f})")

    # Топ-5 самых влиятельных агентов
    print("\n=== ТОП-5 ЛИДЕРОВ ОБЩИНЫ ===")
    leaders = sorted(community.agents, key=lambda x: x.social_weight, reverse=True)[:5]
    for i, agent in enumerate(leaders, 1):
        print(f"{i}. Агент #{agent.id}: вес={agent.social_weight:.2f} "
              f"(O={agent.O:.1f}, C={agent.C:.1f}, E={agent.E:.1f})")

