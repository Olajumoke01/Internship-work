
from sqlalchemy.sql import func, select, text
import random

def person_id_provider(db_connection):
    random_row = db_connection.execute(text("select person_id from person where person_id not in (select person_id from death)")).first()
    return getattr(random_row, "person_id", None)

def birth_year_provider(generic, query_results):
    mu: float = float(query_results[0]["trunc"])
    sigma: float = float(query_results[0]["stddev"])
    return random.gauss(mu,sigma)


def gender_concept_provider(generic, query_results):
    population = [8507, 8532]
    weights = [float(query_results[0]["percentage"]), float(query_results[0]["percentage"])]
    random_value = random.choices(population, weights=weights, k=1)
    if random_value[0] == 8532:
        source_value = 2
    elif random_value[0] == 8507:
        source_value = 1
    return random_value[0], source_value



def race_concept_provider(generic, ethnicity_query_results, race_query_results):
    
    ethnicity_concept_values = [38003563, 38003564]
    weights = [float(ethnicity_query_results[0]["count"]), float(ethnicity_query_results[0]["count"])]
    Erandom_value = random.choices(ethnicity_concept_values, weights=weights, k=1)   
    race_concept_values = [8527, 0, 8516]
    weights = [float(race_query_results[0]["count"]), float(race_query_results[0]["count"]),float(race_query_results[0]["count"]) ]
    Rrandom_value = random.choices(race_concept_values, weights=weights, k=1)
    
    if Erandom_value[0] == 38003563:
        Rrandom_value[0] = 0
        source_value = 5
        ethnicity_value = 5    
    elif Rrandom_value[0] == 8516:
        source_value = 2
        ethnicity_value = 2
    elif Rrandom_value[0] == 8527:
        source_value = 1
        ethnicity_value = 1
    else:
        source_value = 3
        ethnicity_value = 3

    return Rrandom_value[0], source_value, Erandom_value[0], ethnicity_value


def make_null(db_connection):
    return None


def condition_dates_provider(generic):
    condition_start_date: datetime.date = generic.datetime.date(start=2006, end=2011)
    
    condition_end_date: datetime.date = generic.datetime.date(start=2007, end=2011)
    if condition_start_date > condition_end_date:
            condition_end_date = generic.datetime.date(start = condition_start_date.year + 1, end=2012)
    return condition_start_date, condition_end_date
    

   
