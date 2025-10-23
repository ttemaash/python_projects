import file_operations
import os
import random
from faker import Faker


MAGIC_LETTERS = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]


def change_usual_letter(char_skill, MAGIC_LETTERS):
    magic_char_skill = ""
    for letter in char_skill:
        for key, value in MAGIC_LETTERS.items():
            if letter == key:
                magic_char_skill += value
    return magic_char_skill


def main():
    number_of_images = 10
    number_of_skills = 3
    lower_bound_of_skill = 3
    higher_bound_of_skill = 18

    fake = Faker("ru_RU")

    base_dir = os.path.dirname(__file__)
    template_path = os.path.join(base_dir, "src", "charsheet.svg")
    result_folders = os.path.join(base_dir, "output", "svg")
    os.makedirs(result_folders, exist_ok=True)
    result_path = os.path.join(result_folders, "result.svg")

    for image in range(number_of_images):
        char_name = fake.first_name_male()
        char_last_name = fake.last_name_male()
        char_city = fake.city()
        char_profession = fake.job()
        char_strength = random.randint(lower_bound_of_skill, higher_bound_of_skill)
        char_agility = random.randint(lower_bound_of_skill, higher_bound_of_skill)
        char_endurance = random.randint(lower_bound_of_skill, higher_bound_of_skill)
        char_intelligence = random.randint(lower_bound_of_skill, higher_bound_of_skill)
        char_luck = random.randint(lower_bound_of_skill, higher_bound_of_skill)
        unique_skills = random.sample(SKILLS, number_of_skills)
        char_skill_1, char_skill_2, char_skill_3 = unique_skills
        runic_skills = []
        magic_char_skill_1 = change_usual_letter(char_skill_1, MAGIC_LETTERS)
        runic_skills.append(magic_char_skill_1)
        magic_char_skill_2 = change_usual_letter(char_skill_2, MAGIC_LETTERS)
        runic_skills.append(magic_char_skill_2)
        magic_char_skill_3 = change_usual_letter(char_skill_3, MAGIC_LETTERS)
        runic_skills.append(magic_char_skill_3)

        context = {
            "first_name": char_name,
            "last_name": char_last_name,
            "job": char_profession,
            "town": char_city,
            "strength": char_strength,
            "agility": char_agility,
            "endurance": char_endurance,
            "intelligence": char_intelligence,
            "luck": char_luck,
            "skill_1": magic_char_skill_1,
            "skill_2": magic_char_skill_2,
            "skill_3": magic_char_skill_3,
        }

        file_operations.render_template(
            str(template_path),
            str(result_path.replace("result.svg", f"result_{image+1}.svg")),
            context,
        )


if __name__ == "__main__":
    main()
