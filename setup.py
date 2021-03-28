from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(name='gym_pikachu_volleyball',
      version='0.0.1',
      install_requirements=['gym'],
      author="Hoseong Lee",
      author_email="mr.hoseong.lee@gmail.com",
      description="An openai-gym wrapper for pikachu-volleyball",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/MrHoseongLee/gym-pikachu-volleyball",
      packages=find_packages(),
      package_data = {'sprites': ['envs/sprites/*']},
      zip_safe = False
)

