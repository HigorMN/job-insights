from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    max_salary = set()
    for job in data:
        if job["max_salary"] and job["max_salary"].isdigit():
            max_salary.add(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    min_salary = set()
    for job in data:
        if job["min_salary"] and job["min_salary"].isdigit():
            min_salary.add(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary ou max_salary não existe")

    if not isinstance(salary, (int, str)):
        raise ValueError("O salário deve ser um número inteiro ou uma string")

    if (
        type(job["max_salary"]) != int
        and type(job["max_salary"]) != str
        or type(job["min_salary"]) != int
        and type(job["min_salary"]) != str
    ):
        raise ValueError("min_salary ou max_salary não é um número inteiro")

    if job["min_salary"] is None or job["max_salary"] is None:
        raise ValueError("max_salary ou min_salary não pode ser None")

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary é maior que max_salary")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
