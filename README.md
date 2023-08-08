# Music Recommender Chatbot on Dockers

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#objectives">Objectives</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#setup">Setup</a></li>
    <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About The Project
In this age of rapid technological progress, the seamless integration of music and technology becomes increasingly vital. With a sophisticated music recommendation system driven by mood analysis, individuals can effortlessly find solace in soothing tunes that align with their emotional state, offering an invaluable means to alleviate stress and elevate their listening experience.

### Objectives
In this project, we would be utlizing open-source tools to make Aca Pella that recommends songs based on the tone of the conservation:
- Converse with Aca Pella
- Analyze the tone of the converstation & intention using [SpaCY](https://spacy.io/) and [Rasa](https://rasa.com/) architects
- Query song recommendations based on tone through API

### Built With
- Deployment - [Docker Engine](https://www.docker.com/)
- Emotional Analysis -  [SpaCY](https://spacy.io/) and [Rasa](https://rasa.com/) architect and pre-trained model
- Song Recommendation Database - [Last.FM](https://www.last.fm/)

## Setup

### Prerequisites

- Install [Docker Engine](https://docs.docker.com/engine/) with docker-compose

Test installation by running these commands:
```sh
$ docker --help
$ docker compose --help
```

### Installation
Clone this repository:
```sh
$ git clone https://github.com/cosettekay/Music-Recommendation-Bot.git
```
You must give the correct permission to the directory of the project:
```sh
$ chmod 777 ./Music-Recommendation-Bot
``` 

It is highly recommend to train the model on your local system to ensure that permissions and files necessary are avaible on your system, run the code below to train:
```sh
$ docker run -v $(pwd):/app  rasa/rasa:3.6.2-full train --domain domain.yml --data data --out models
```

Now you are all set and ready to setup and use Aca Pella!

## Usage

__*Notice that you must first aquire your own Last.FM API key before continuing...__

- Aquire [Last.FM API Key](https://www.last.fm/api) by making an account, it is completely free

- Copy your API Key int the following varible found in actions/actions.py [API_KEY = 'enter your Last.FM API'](https://github.com/cosettekay/Music-Recommendation-Bot/blob/2d3ba8d541ed20286fb06cb84bde47b9c62045ec/actions/actions.py#L16)

Once that is complete, you're read to build your bot

The following code only has to be ran once:
```sh
$ docker build -t my_action_image
```

Running the bot can simiply be ran by using Docker Compose command:
```sh
$ docker compose run rasa
```
Now you can chat with Aca Pella

## Contact

Cosette Tabucol:
- Email - cmtabucol@cpp.edu
- LinkedIn - https://www.linkedin.com/in/cosette-tabucol-a914751b7/

## Acknowledgements

- [Last.FM API](https://www.last.fm/api)
- [Music & Me](https://github.com/Srishti20022/Music-me-Chatbot_song_recommendor_system-)
- [Rasa Assistant on Docker](https://rasa.com/docs/rasa/docker/building-in-docker/)
- [SpaCy Pre-Trained Model](https://spacy.io/models/en)
- [Rasa Data Templates](https://github.com/cedextech/rasa-chatbot-templates/tree/master)
- [Rasa Mood Training Data](https://github.com/RasaHQ/NLU-training-data/tree/main/mood)
- [Getting Music Data with the Last.fm API using Python](https://www.dataquest.io/blog/last-fm-api-python/)

