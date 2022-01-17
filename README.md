# Foobar Factory

### Settings

params.py file can be edited to parametrize the project.
Project runs with the default parameters

- time_reducer_factor : increase or reduce task time proportionally
- foobar_to_build_in_one_cycle : Number of foobar to create in one cycle ( after testings, 3 was the fastest)
- max_bot : Trigger to stop the Foobar Factory

### Launch program

`python main.py`

### Launch test

`pip install coverage`
`coverage run -m unittest discover tests`

### Launch coverage report

`coverage report -m`
