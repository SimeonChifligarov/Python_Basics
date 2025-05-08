def estimate_project_hours(architect_name: str, project_count: int) -> str:
    """
    Calculates how many hours an architect needs to finish given number of projects.

    Args:
        architect_name: name of the architect
        project_count: number of projects to complete

    Returns:
        A message with the name and calculated hours
    """
    if not architect_name.strip() or project_count < 0 or project_count > 100:
        return 'Invalid input.'

    total_hours = project_count * 3
    return f'The architect {architect_name} will need {total_hours} hours to complete {project_count} project/s.'


if __name__ == '__main__':
    input_architect: str = input()
    input_projects: int = int(input())

    output_message: str = estimate_project_hours(
        architect_name=input_architect,
        project_count=input_projects
    )

    print(output_message)
