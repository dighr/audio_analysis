# Audio Analysis
This project is divided into two parts:
- an API is created to transcribe, translate, and analyze the sentiment values of audio files using multiple commercial APIs. 
- Determining the accuracy of multiple commercial transcription models by transcribing 4070 audio files against each model 
### Prerequisites
All of the following needs to be downloaded in your device
 * Python 3.6
 * virtualenv
 * pip
 * GOOGLE cloud Credentials
 * Deepspeech pre-trained model

### Setting up
 * download the github repo  
```
  git clone https://github.com/dighr/audio_analysis.git
  
``` 
* Navigate to the cloned repo
* Create a python virtualenv 
```
virtualenv -p python3 env
```
* Activate the virtual environment
```
source env/bin/activate
```
* Download all the dependencies
```
pip install -r requirements.txt
```

* Add the GOOGLE_APPLICATION_CREDENTIALS into the enviroment variables
  * If you don't have an account yet, create an account https://cloud.google.com/
  * Within the google cloud console, create a new project
  * Within the created project, enable the NLP API and the audio-to-text API
  * Create a service
  * Download the credentials of the created service as JSON
  * Add an enviroment variable named GOOGLE_APPLICATION_CREDENTIALS 
    and point the downloaded JSON file into it
       * In linux, just execute the following in the terminal
       ```
         export  GOOGLE_APPLICATION_CREDENTIALS=path-to-the-downloaded-json-file
       ```
       
  * Add an environment variable to store the private API keys of both Watson and Azure
   
    
## Getting Started
Assuming that the previous section is complete, you can start the server by executing the following in  a terminal
 ```
python manage.py runserver
 ```         
 
## Making API calls

### language_code for both 'audio/transcribe' and 'audio/analyze'
The API calls to transcribe audios require a language_code as a parameter to be passed in within the body.
Find the correct language code from the following URL
https://cloud.google.com/speech-to-text/docs/languages

### language_code for both 'text/analyze' and text/translate'
Both 'text/analyze' and 'text/translate' API also requires 'language_code' as a parameter when making an API call. 
Use the correct ISO-639-1 Code value for 'language_code from the link below
https://cloud.google.com/translate/docs/languages

### API CALLS
To analyze a text, make a post request  to the following URL
PASS in both text=text_to_be_analyzed and method=google into the body
 ```
 http://localhost:PORT/text/analyze
 ```
 
To translate a text, make a post request to the following URL
Provide  both 'text' (text_to_be_translated) and 'source_language' (Explained above) as an input to make the translation
 ```
 http://localhost:PORT/text/translate
 ```

 To transcribe an audio file, make a post request to the following URL
 ```
 http://localhost:PORT/audio/transcribe
 ```
 Attach the audio file within the body of the request in the following format
'file=audio_file_path'
pass in the 'language_code' parameter into the body


 To analyze an audio file, make a post request to the following URL
 ```
 http://localhost:PORT/audio/analyze
 ```
 Attach the audio file within the body of the request in the following format
'file=audio_file_path'
pass in the language_code parameter into the body

 
## Sample Outputs
 
<details>
  <summary>
        Sample out of a text analysis response of a portion of an article taken from CNN
  </summary>
 <p>

 ```json
    {
        "status": 1,
        "analysis": {
            "sentences": [
                {
                    "text": {
                        "content": "President Donald Trump told special counsel Robert Mueller in writing that Roger Stone did not tell him about WikiLeaks, nor was he told about the 2016 Trump Tower meeting between his son, campaign officials and a Russian lawyer promising dirt on Hillary Clinton, according to two sources familiar with the matter.",
                        "beginOffset": -1
                    },
                    "sentiment": {}
                },
                {
                    "text": {
                        "content": "One source described the President's answers without providing any direct quotes and said the President made clear he was answering to the best of his recollection.",
                        "beginOffset": -1
                    },
                    "sentiment": {
                        "magnitude": 0.4000000059604645,
                        "score": 0.4000000059604645
                    }
                },
                {
                    "text": {
                        "content": "This is the first insight into how the President responded to the Mueller team's written questions -- a key unknown as Mueller aims to wrap up his investigation and prepare his final report.",
                        "beginOffset": -1
                    },
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                }
            ],
            "entities": [
                {
                    "name": "Donald Trump",
                    "type": "PERSON",
                    "metadata": {
                        "wikipedia_url": "https://en.wikipedia.org/wiki/Donald_Trump",
                        "mid": "/m/0cqt90"
                    },
                    "salience": 0.37138432264328003,
                    "mentions": [
                        {
                            "text": {
                                "content": "Donald Trump",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        },
                        {
                            "text": {
                                "content": "President",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        },
                        {
                            "text": {
                                "content": "President",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        },
                        {
                            "text": {
                                "content": "President",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.800000011920929,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "Robert Mueller",
                    "type": "PERSON",
                    "metadata": {
                        "wikipedia_url": "https://en.wikipedia.org/wiki/Robert_Mueller",
                        "mid": "/m/02djmh"
                    },
                    "salience": 0.2821030616760254,
                    "mentions": [
                        {
                            "text": {
                                "content": "Robert Mueller",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        },
                        {
                            "text": {
                                "content": "counsel",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        },
                        {
                            "text": {
                                "content": "Mueller",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {}
                        },
                        {
                            "text": {
                                "content": "Mueller",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {
                        "magnitude": 1.100000023841858,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "Roger Stone",
                    "type": "PERSON",
                    "metadata": {
                        "wikipedia_url": "https://en.wikipedia.org/wiki/Roger_Stone",
                        "mid": "/m/05r8b8"
                    },
                    "salience": 0.157715305685997,
                    "mentions": [
                        {
                            "text": {
                                "content": "Roger Stone",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.30000001192092896,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "meeting",
                    "type": "EVENT",
                    "salience": 0.018298445269465446,
                    "mentions": [
                        {
                            "text": {
                                "content": "meeting",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "sources",
                    "type": "PERSON",
                    "salience": 0.014273649081587791,
                    "mentions": [
                        {
                            "text": {
                                "content": "sources",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "matter",
                    "type": "OTHER",
                    "salience": 0.012554647400975227,
                    "mentions": [
                        {
                            "text": {
                                "content": "matter",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "campaign officials",
                    "type": "PERSON",
                    "salience": 0.012402627617120743,
                    "mentions": [
                        {
                            "text": {
                                "content": "campaign officials",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "lawyer",
                    "type": "PERSON",
                    "salience": 0.012402627617120743,
                    "mentions": [
                        {
                            "text": {
                                "content": "lawyer",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "son",
                    "type": "PERSON",
                    "salience": 0.012402627617120743,
                    "mentions": [
                        {
                            "text": {
                                "content": "son",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "dirt",
                    "type": "OTHER",
                    "salience": 0.012402627617120743,
                    "mentions": [
                        {
                            "text": {
                                "content": "dirt",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "Trump Tower",
                    "type": "LOCATION",
                    "metadata": {
                        "wikipedia_url": "https://en.wikipedia.org/wiki/Trump_Tower",
                        "mid": "/m/04qqj8"
                    },
                    "salience": 0.01088088471442461,
                    "mentions": [
                        {
                            "text": {
                                "content": "Trump Tower",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "WikiLeaks",
                    "type": "ORGANIZATION",
                    "metadata": {
                        "wikipedia_url": "https://en.wikipedia.org/wiki/WikiLeaks",
                        "mid": "/m/027m_21"
                    },
                    "salience": 0.01088088471442461,
                    "mentions": [
                        {
                            "text": {
                                "content": "WikiLeaks",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "source",
                    "type": "OTHER",
                    "salience": 0.009939493611454964,
                    "mentions": [
                        {
                            "text": {
                                "content": "source",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "President",
                    "type": "PERSON",
                    "salience": 0.00810279045253992,
                    "mentions": [
                        {
                            "text": {
                                "content": "President",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "Hillary Clinton",
                    "type": "PERSON",
                    "metadata": {
                        "wikipedia_url": "https://en.wikipedia.org/wiki/Hillary_Clinton",
                        "mid": "/m/0d06m5"
                    },
                    "salience": 0.007359262555837631,
                    "mentions": [
                        {
                            "text": {
                                "content": "Hillary Clinton",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "Russian",
                    "type": "LOCATION",
                    "salience": 0.007359262555837631,
                    "mentions": [
                        {
                            "text": {
                                "content": "Russian",
                                "beginOffset": -1
                            },
                            "type": "PROPER",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "insight",
                    "type": "OTHER",
                    "salience": 0.007166363764554262,
                    "mentions": [
                        {
                            "text": {
                                "content": "insight",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.6000000238418579,
                                "score": 0.6000000238418579
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.699999988079071,
                        "score": 0.30000001192092896
                    }
                },
                {
                    "name": "answers",
                    "type": "OTHER",
                    "salience": 0.0065950071439146996,
                    "mentions": [
                        {
                            "text": {
                                "content": "answers",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "quotes",
                    "type": "OTHER",
                    "salience": 0.004241628106683493,
                    "mentions": [
                        {
                            "text": {
                                "content": "quotes",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "questions",
                    "type": "OTHER",
                    "salience": 0.004169093910604715,
                    "mentions": [
                        {
                            "text": {
                                "content": "questions",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "team",
                    "type": "ORGANIZATION",
                    "salience": 0.004169093910604715,
                    "mentions": [
                        {
                            "text": {
                                "content": "team",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "unknown",
                    "type": "OTHER",
                    "salience": 0.004169093910604715,
                    "mentions": [
                        {
                            "text": {
                                "content": "unknown",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "investigation",
                    "type": "EVENT",
                    "salience": 0.0029199873097240925,
                    "mentions": [
                        {
                            "text": {
                                "content": "investigation",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {}
                        }
                    ],
                    "sentiment": {}
                },
                {
                    "name": "report",
                    "type": "WORK_OF_ART",
                    "salience": 0.002428423846140504,
                    "mentions": [
                        {
                            "text": {
                                "content": "report",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "best",
                    "type": "OTHER",
                    "salience": 0.0018394036451354623,
                    "mentions": [
                        {
                            "text": {
                                "content": "best",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.10000000149011612,
                                "score": 0.10000000149011612
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.10000000149011612,
                        "score": 0.10000000149011612
                    }
                },
                {
                    "name": "recollection",
                    "type": "OTHER",
                    "salience": 0.0018394036451354623,
                    "mentions": [
                        {
                            "text": {
                                "content": "recollection",
                                "beginOffset": -1
                            },
                            "type": "COMMON",
                            "sentiment": {
                                "magnitude": 0.4000000059604645,
                                "score": 0.4000000059604645
                            }
                        }
                    ],
                    "sentiment": {
                        "magnitude": 0.4000000059604645,
                        "score": 0.4000000059604645
                    }
                }
            ],
            "documentSentiment": {
                "magnitude": 0.5,
                "score": 0.10000000149011612
            },
            "language": "en"
        }
    }
 ```
 </p>
</details>
 
 <details>
  <summary>
      Sample output of the audio analysis post request for the following ted talk
      https://www.ted.com/talks/brene_brown_on_vulnerability?language=en
  </summary>
 <p>
 
 ```
 {
    "status": 1,
    "audio_text": "TED Talks recorded live at Ted conference and partner events this episode features professor of Social Work brene Brown here's brene Brown I'll start with this a couple years ago an event planner called me cuz I was going to do a speaking event and she called and she said I'm really struggling with how to write about you on the little flyer and I thought will what's the struggle and she said well I saw you speak and I'm going to call you a researcher I think that I'm afraid if I call your research or no one will, because they'll think you're boring and irrelevant ,okay and she said so but the thing I liked about your talk as you know you're a Storyteller so I think what I'll do is just call you a Storyteller and of course the academic insecure part of me was like you're going to call me or what and she said I'm going to call you a Storyteller and I was like why not magic pixie let me think about this for a second I tried to call Devon my courage and I thought you know I am a Storyteller I'm a qualitative researcher I collect story that's what I do and maybe stories are just data with a soul you know and maybe I'm just a Storyteller so I said you know what why don't you just say I'm a researcher storyteller ,and she went there's no such thing so I'm a researcher Storyteller and I'm going to talk to you today we're talking about expanding perception until I want to talk to you and tell him stories about a piece of my research that fundamentally expanding my perception and really actually change the way that I live and love and work and parent and this is where my story starts when I was a young researcher doctoral student my first year I had a research Professor who said here's the thing if you cannot measure it it does not exist but I thought he was just sweet-talking me I was like really and he's like absolutely ,I understand that I have a Bachelors in Social Work a masters in social work and was getting my PHD in social work to my entire academic career was surrounded by people who kind of believed in the life's messy love it you know and I'm more of the life's messy clean it up organize it and put it into a Bento Box and so to think I have found my way to found a career that takes me and I really one of the big saying and in social work is lean into the discomfort of the work and I'm like you know not discomfort upside the head and move it over and get all A's that's my that was my mantra that was very excited about that ,and so I thought you know what this is a queer for me because I am interested in some messy topics but I want to be able to make them not messy I want to understand them I want to hack into these things that I know are important and lay the code out for everyone to see so where I started was with connection because by the time your social worker for 10 years what you realize is that connection is why we're here it's what gives purpose and meaning to our lives this is this is what it's all about it doesn't matter whether you talk to people who work in social justice and mental health and abuse and neglect what we know is that connection the ability to feel connected is neurobiological ,that's how we're wired it's why we're here so I thought you know what I'm going to start with connection we know that that situation where you get an evaluation from your boss and she tells you 37 things that you do really awesome and one thing that you can't do an opportunity for growth and all you can think about is that opportunity for growth right well apparently this is the way my work went as well because when you ask people about love they tell you about heartbreak when you ask people about belonging they'll tell you their most excruciating experiences of being excluded and when you ask people about connection the stories they told me where about disconnection it's a very quickly really about six weeks into this research ,I ran into this unnamed thing that absolutely unraveled connection in a way that I didn't understand her had never seen and so I pull back out of the research and thought I need to figure out what this is and it turned out to be shame and Shane is really easily understood as a fear of disconnection is there something about me that if other people know it or see it that I won't be worthy of connection the things I can tell you about it it's Universal we all have that the only people who don't experience shame have no capacity for human empathy or connection no one wants to talk about it unless you talk about it the more you have it what under pend ,this shame this I'm not good enough which we all know that feeling I'm not blank enough I'm not spending a fortune. Beautiful not smart enough promoted enough the thing that underpinned this was excruciating vulnerability this idea of an order for connection to happen we have to allow ourselves to be seen really scene and you know how I feel about vulnerability I hate vulnerability and so I thought this is my chance to beat it back with my measuring stick I'm going in I'm going to figure this stuff out I'm going to spend a year I'm going to totally deconstruct shame I'm going to understand how bone ability works and I'm going to outsmart it thought I was ready and I was ,excited as you know it's not going to turn out well you know that so I can tell you a lot about shame but I have to buy everyone else a time but here's what I can tell you that it boils down to and this may be one of the most important things I've ever learned and the decade of doing this research my 1 years turned into 6 years thousands of stories hundreds of long interviews focus groups at one point people were sending me journal pages and sending me their stories thousands of pieces of data and six years and I kind of got a handle on it I kind of understood this is what shame is it ,at work I read a book I published a theory but something was not okay and what it was is that if I roughly took the people I interviewed and divided them into people who really have a sense of worthiness that's what this comes down to it since the poor thing that they have a strong sense of love and belonging and folks who struggle for it and folks who are always wondering if they're good enough there was only one variable that separated the people who have a strong sense of love and belonging and the people who really struggle for it and that was the people who have a strong sense of love and belonging believe they're worthy of love and belonging ,they believe there were they and to me the hard part of the one thing that keeps us out of connection is our fear that we're not worthy of connection what's something that personally and professionally I felt like I needed to understand better so what I did is I took all of the interviews where I saw where they guess where I saw people letting that way and just looked at those what do these people have in common and I have I have a slight office supply addiction but with another talk so I had to Manila notebook manila folder and I had a Sharpie and I was like what am I going to call this research in the first words that came to my mind where wholehearted ,he's our kind of hole hearted people living from this deep sense of worthiness I rode the top of the manila folder and I started looking at the data in fact I did it first and it's very full and afford a very intensive data analysis why I went back pull these interviews pull the stories pull the internet what's the what's the thing what's the pattern my husband left town with the kids because I always go into the kind of Jackson Pollock crazy thing where I just like riding and then going and kind of just in my researcher mode and so here's what I found what they had in common was it since of courage and I wanted separate courage and bravery for you for a minute Courage the original ,definition of courage when it first came into English language is from the Latin word Cur mini heart and the original definition was to tell the story of who you are with your whole heart hits of these folks had very simply the courage to be imperfect they had the compassion to be kind of themselves first and then to others because as it turns out we can't practice compassion with other people if we can't treat ourselves kindly and the last was they had a connection and this was the hard part as a result of authenticity they were willing to let go of who they thought they should be in order to be who they were which is you have to absolutely do that for connection ,the other thing that they had in common was that they fully Embrace vulnerability they believed that what made them vulnerable made them beautiful they didn't talk about vulnerability being comfortable nor did they really talk about it being excruciating as I had heard it earlier in the shame interviewing they just talked about it being necessary they talked about the willingness to say I love you first the willingness to ,do something where there are no guarantees the willingness to breathe through waiting for the doctor to call after your mammogram who willing to invest in a relationship that may or may not work out they thought this was fundamental I personally thought it was betrayal I could not believe I had pledged allegiance to research where are job here the definition of research is to control control and predict to study phenomenon for the reason for the explicit reason to control and predict and now my very you my mission to control and predict had turned up the answer that the way to live is with all ,I just thought control at predicting this led to a little breakdown which actually looks more like that and it did it led to a I caught a break down my therapist called in a spiritual awakening it's going to lightning sounds better than break down but I assure you it was a breakdown and I had to put my date away and go find a therapist let me tell you something you know who you are when you call your friends and say I think I need to see somebody do you have any recommendations thinking about 5 my friends like I wouldn't want to be your therapist ,I'm just saying you don't like don't bring a measuring stick okay so I found a therapist my first meeting with her Diana I brought in my list of the way the wholehearted live and I sat down and she said you know how are you and I said I'm going to let you know I'm okay and she said what's going on and I said therapist who sees therapist because we have to go to those because their BS meters are good so I said here's the thing I'm struggling and she's struggling I said well I have a ,ability issue and you know and I know that vulnerability is kind of decor a shame and fear in our struggle for worthiness but it appears that it's also the birthplace of joy of creativity a belonging of love and I I think I have a problem and I just I need some help and I said but here's the thing no family stuff no childhood should I just I just need some strategy Adele there she goes like this ,and then I said it's bad right she said it's neither good nor bad it just is what it is and I said oh my God this is going to stink and it did and it didn't and it took about a year and you know how their people that like when they realized that vulnerability and tenderness are important that they kind of surrender and walk into it a that's not me and B I don't even hang out with people like that for me it was a year-long street fight it was a slugfest ,phone really pushed I pushed back I lost the fight but probably want my life back and so then I went back into the research and spent the next couple of years really trying to understand what they the wholehearted what the choices they were making it and what what is what what are we doing with all Mobility why do we struggle with it too much am I alone and struggling with an ability no so this is what I learned we numb vulnerability when were waiting for the call it was funny I sent something out on Twitter and on Facebook that says how would you define vulnerability what makes you feel vulnerable and within an hour and a half ahead of 150 responses ,cuz I wanted to know if you know what was out there having to ask my husband for help cuz I'm sick and we're newly married initiating sex with my husband and is she dating sex with my wife being turned down asking someone out waiting for the doctor to call back getting laid off laying off people this is the world we live in we live in a vulnerable world and one of the ways we deal with it as we known vulnerability and I think there's evidence and it's not the only reason this evidence exists that I think that there is a huge cock we are the most in debt obese ,kitten and medicated adult cohort in US history the problem is and I learned this from the research that you cannot selectively numb emotion you can't say here's the bad stuff here is vulnerability here's grief here Shane here's fear here's disappointment I don't want to feel these I'm going to have a couple of beers in a banana nut muffin I don't want to feel these and I know that's why I know that's knowing laughter I I hack into your lives for a living I know that's God new cat dumb those hard feeling without numbing the other FXR ,you cannot possibly know so when we know um those wee Nam gioi we not gratitude we numb happiness and then we are miserable and we are looking for purpose and meaning and then we feel vulnerable so then we have a couple of beers in a banana nut muffin and it becomes dangerous cycle one of the things that I think that we need to think about is why and how we numb and it doesn't just have to be addiction the other thing we do is we make everything is uncertain certain religion has gone from a belief and faith in mystery 2 certainty I'm right ,shut up that's it just certain the more afraid we are the more vulnerable you are the more afraid we are this is what politics looks like today there's no discourse anymore there's no conversation there's just blame blame as described in the research a way to discharge pain and discomfort we perfect if there's anyone who wants their life to look like this it would be me but it doesn't work because what we do is we take fat from her butt and put it in our cheeks which death I hope in a hundred years people will look back and go ,and we perfect most dangerously our children let me tell you what we think about children they're hardwired for struggle when they get here when you stole those perfect little babies in your hand our job is not to say look at her she's perfect my job is just to keep her perfect make sure she make the tennis team by fifth grade and yell by seventh grade a job our job is to look until you know what you're imperfect and you're wired for struggle but you are worthy of love and belonging that's our job show me a generation of kids raised like that and will end the problems I think that we see today we pretend that what we do doesn't have an effect on people we do that in our personal lies we do that ,weather at the bail out and oil spill I recall we pretend like what we're doing. They have a huge impact on other people I would say the company this is not our first rodeo people we just need you to be authentic and real and say we're sorry we'll fix it but there's another way and I'll leave you with this this is what I found to let ourselves be seen deeply sing voice thing to love with our whole hearts even though there's no guarantee and that's really hard and I can tell you the parent that's excruciating Lee difficult ,to practice gratitude and joy and those moments of kind of Terror when we were wondering can I love you this much can I believe in this is passionately can I be this Fierce about this just to be able to stop and instead of catastrophizing what might happen to say I'm just so grateful because I feel this wonderful means I'm alive and the last which I think is probably the most important it's a believe that were enough because when we work from a place I believe that says I'm enough then we stop screaming and start listening for Kinder and gentler to the people around us then we're Kinder and gentler Char South that's all I have ,that was brene brown recorded at tedx Houston in Houston Texas June 2010 for more information on Ted visit ted.com ,",
    "audio_analysis": {
        "sentences": [
            {
                "text": {
                    "content": "TED Talks recorded live at Ted conference and partner events this episode features professor of Social Work brene Brown here's brene Brown I'll start with this a couple years ago an event planner called me cuz I was going to do a speaking event and she called and she said I'm really struggling with how to write about you on the little flyer and I thought will what's the struggle and she said well I saw you speak and I'm going to call you a researcher I think that I'm afraid if I call your research or no one will, because they'll think you're boring and irrelevant ,okay and she said so but the thing I liked about your talk as you know you're a Storyteller so I think what I'll do is just call you a Storyteller and of course the academic insecure part of me was like you're going to call me or what and she said I'm going to call you a Storyteller and I was like why not magic pixie let me think about this for a second I tried to call Devon my courage and I thought you know I am a Storyteller I'm a qualitative researcher I collect story that's what I do and maybe stories are just data with a soul you know and maybe I'm just a Storyteller so I said you know what why",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "text": {
                    "content": "don't you just say I'm a researcher storyteller ,and she went there's no such thing so I'm a researcher Storyteller and I'm going to talk to you today we're talking about expanding perception until I want to talk to you and tell him stories about a piece of my research that fundamentally expanding my perception and really actually change the way that I live and love and work and parent and this is where my story starts when I was a young researcher doctoral student my first year I had a research Professor who said here's the thing if you cannot measure it it does not exist but I thought he was just sweet-talking me I was like really and he's like absolutely ,I understand that I have a Bachelors in Social Work a masters in social work and was getting my PHD in social work to my entire academic career was surrounded by people who kind of believed in the life's messy love it you know and I'm more of the life's messy clean it up organize it and put it into a Bento Box and so to think I have found my way to found a career that takes me and I really one of the big saying and in social work is lean into the discomfort of the work and I'm like you know not discomfort upside the head and",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": 0.30000001192092896
                }
            },
            {
                "text": {
                    "content": "move it over and get all A's that's my that was my mantra that was very excited about that ,and so I thought you know what this is a queer for me because I am interested in some messy topics but I want to be able to make them not messy I want to understand them I want to hack into these things that I know are important and lay the code out for everyone to see so where I started was with connection because by the time your social worker for 10 years what you realize is that connection is why we're here it's what gives purpose and meaning to our lives this is this is what it's all about it doesn't matter whether you talk to people who work in social justice and mental health and abuse and neglect what we know is that connection the ability to feel connected is neurobiological ,that's how we're wired it's why we're here so I thought you know what I'm going to start with connection we know that that situation where you get an evaluation from your boss and she tells you 37 things that you do really awesome and one thing that you can't do an opportunity for growth and all you can think about is that opportunity for growth right well apparently this is the way my work went as well because when you ask",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": 0.4000000059604645
                }
            },
            {
                "text": {
                    "content": "people about love they tell you about heartbreak when you ask people about belonging they'll tell you their most excruciating experiences of being excluded and when you ask people about connection the stories they told me where about disconnection it's a very quickly really about six weeks into this research ,I ran into this unnamed thing that absolutely unraveled connection in a way that I didn't understand her had never seen and so I pull back out of the research and thought I need to figure out what this is and it turned out to be shame and Shane is really easily understood as a fear of disconnection is there something about me that if other people know it or see it that I won't be worthy of connection the things I can tell you about it it's Universal we all have that the only people who don't experience shame have no capacity for human empathy or connection no one wants to talk about it unless you talk about it the more you have it what under pend ,this shame this I'm not good enough which we all know that feeling I'm not blank enough I'm not spending a fortune.",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "text": {
                    "content": "Beautiful not smart enough promoted enough the thing that underpinned this was excruciating vulnerability this idea of an order for connection to happen we have to allow ourselves to be seen really scene and you know how I feel about vulnerability I hate vulnerability and so I thought this is my chance to beat it back with my measuring stick I'm going in I'm going to figure this stuff out I'm going to spend a year I'm going to totally deconstruct shame I'm going to understand how bone ability works and I'm going to outsmart it thought I was ready and I was ,excited as you know it's not going to turn out well you know that so I can tell you a lot about shame but I have to buy everyone else a time but here's what I can tell you that it boils down to and this may be one of the most important things I've ever learned and the decade of doing this research my 1 years turned into 6 years thousands of stories hundreds of long interviews focus groups at one point people were sending me journal pages and sending me their stories thousands of pieces of data and six years and I kind of got a handle on it I kind of understood this is what shame is it ,at work I read a book I published a theory but something was not okay",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "text": {
                    "content": "and what it was is that if I roughly took the people I interviewed and divided them into people who really have a sense of worthiness that's what this comes down to it since the poor thing that they have a strong sense of love and belonging and folks who struggle for it and folks who are always wondering if they're good enough there was only one variable that separated the people who have a strong sense of love and belonging and the people who really struggle for it and that was the people who have a strong sense of love and belonging believe they're worthy of love and belonging ,they believe there were they and to me the hard part of the one thing that keeps us out of connection is our fear that we're not worthy of connection what's something that personally and professionally I felt like I needed to understand better so what I did is I took all of the interviews where I saw where they guess where I saw people letting that way and just looked at those what do these people have in common and I have I have a slight office supply addiction but with another talk so I had to Manila notebook manila folder and I had a Sharpie and I was like what am I going to call this research in the first words that came to my mind where wholehearted ,he's our",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "text": {
                    "content": "kind of hole hearted people living from this deep sense of worthiness I rode the top of the manila folder and I started looking at the data in fact I did it first and it's very full and afford a very intensive data analysis why I went back pull these interviews pull the stories pull the internet what's the what's the thing what's the pattern my husband left town with the kids because I always go into the kind of Jackson Pollock crazy thing where I just like riding and then going and kind of just in my researcher mode and so here's what I found what they had in common was it since of courage and I wanted separate courage and bravery for you for a minute Courage the original ,definition of courage when it first came into English language is from the Latin word Cur mini heart and the original definition was to tell the story of who you are with your whole heart hits of these folks had very simply the courage to be imperfect they had the compassion to be kind of themselves first and then to others because as it turns out we can't practice compassion with other people if we can't treat ourselves kindly and the last was they had a connection and this was the hard part as a result of authenticity they were willing to let go of who they thought they should be",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "text": {
                    "content": "in order to be who they were which is you have to absolutely do that for connection ,the other thing that they had in common was that they fully Embrace vulnerability they believed that what made them vulnerable made them beautiful they didn't talk about vulnerability being comfortable nor did they really talk about it being excruciating as I had heard it earlier in the shame interviewing they just talked about it being necessary they talked about the willingness to say I love you first the willingness to ,do something where there are no guarantees the willingness to breathe through waiting for the doctor to call after your mammogram who willing to invest in a relationship that may or may not work out they thought this was fundamental I personally thought it was betrayal I could not believe I had pledged allegiance to research where are job here the definition of research is to control control and predict to study phenomenon for the reason for the explicit reason to control and predict and now my very you my mission to control and predict had turned up the answer that the way to live is with all ,I just thought control at predicting this led to a little breakdown which actually looks more like that and it did it led to a I caught a break down my therapist called in a spiritual awakening it's going to lightning sounds better than break down but I assure",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "text": {
                    "content": "you it was a breakdown and I had to put my date away and go find a therapist let me tell you something you know who you are when you call your friends and say I think I need to see somebody do you have any recommendations thinking about 5 my friends like I wouldn't want to be your therapist ,I'm just saying you don't like don't bring a measuring stick okay so I found a therapist my first meeting with her Diana I brought in my list of the way the wholehearted live and I sat down and she said you know how are you and I said I'm going to let you know I'm okay and she said what's going on and I said therapist who sees therapist because we have to go to those because their BS meters are good so I said here's the thing I'm struggling and she's struggling I said well I have a ,ability issue and you know and I know that vulnerability is kind of decor a shame and fear in our struggle for worthiness but it appears that it's also the birthplace of joy of creativity a belonging of love and I I think I have a problem and I just I need some help and I said but here's the thing no family stuff no childhood should I just I just need some strategy Adele there she",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": 0.30000001192092896
                }
            },
            {
                "text": {
                    "content": "goes like this ,and then I said it's bad right she said it's neither good nor bad it just is what it is and I said oh my God this is going to stink and it did and it didn't and it took about a year and you know how their people that like when they realized that vulnerability and tenderness are important that they kind of surrender and walk into it a that's not me and B I don't even hang out with people like that for me it was a year-long street fight it was a slugfest ,phone really pushed I pushed back I lost the fight but probably want my life back and so then I went back into the research and spent the next couple of years really trying to understand what they the wholehearted what the choices they were making it and what what is what what are we doing with all Mobility why do we struggle with it too much am I alone and struggling with an ability no so this is what I learned we numb vulnerability when were waiting for the call it was funny I sent something out on Twitter and on Facebook that says how would you define vulnerability what makes you feel vulnerable and within an hour and a half ahead of 150 responses ,cuz I wanted to know if you know what was out there having to ask my",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.800000011920929,
                    "score": -0.800000011920929
                }
            },
            {
                "text": {
                    "content": "husband for help cuz I'm sick and we're newly married initiating sex with my husband and is she dating sex with my wife being turned down asking someone out waiting for the doctor to call back getting laid off laying off people this is the world we live in we live in a vulnerable world and one of the ways we deal with it as we known vulnerability and I think there's evidence and it's not the only reason this evidence exists that I think that there is a huge cock we are the most in debt obese ,kitten and medicated adult cohort in US history the problem is and I learned this from the research that you cannot selectively numb emotion you can't say here's the bad stuff here is vulnerability here's grief here Shane here's fear here's disappointment I don't want to feel these I'm going to have a couple of beers in a banana nut muffin I don't want to feel these and I know that's why I know that's knowing laughter I I hack into your lives for a living I know that's God new cat dumb those hard feeling without numbing the other FXR ,you cannot possibly know so when we know um those wee Nam gioi we not gratitude we numb happiness and then we are miserable and we are looking for purpose and meaning and",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.800000011920929,
                    "score": -0.800000011920929
                }
            },
            {
                "text": {
                    "content": "then we feel vulnerable so then we have a couple of beers in a banana nut muffin and it becomes dangerous cycle one of the things that I think that we need to think about is why and how we numb and it doesn't just have to be addiction the other thing we do is we make everything is uncertain certain religion has gone from a belief and faith in mystery 2 certainty I'm right ,shut up that's it just certain the more afraid we are the more vulnerable you are the more afraid we are this is what politics looks like today there's no discourse anymore there's no conversation there's just blame blame as described in the research a way to discharge pain and discomfort we perfect if there's anyone who wants their life to look like this it would be me but it doesn't work because what we do is we take fat from her butt and put it in our cheeks which death I hope in a hundred years people will look back and go ,and we perfect most dangerously our children let me tell you what we think about children they're hardwired for struggle when they get here when you stole those perfect little babies in your hand our job is not to say look at her she's perfect my job is just to keep her perfect make sure she make the tennis team",
                    "beginOffset": -1
                },
                "sentiment": {}
            },
            {
                "text": {
                    "content": "by fifth grade and yell by seventh grade a job our job is to look until you know what you're imperfect and you're wired for struggle but you are worthy of love and belonging that's our job show me a generation of kids raised like that and will end the problems I think that we see today we pretend that what we do doesn't have an effect on people we do that in our personal lies we do that ,weather at the bail out and oil spill I recall we pretend like what we're doing.",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.5,
                    "score": 0.5
                }
            },
            {
                "text": {
                    "content": "They have a huge impact on other people I would say the company this is not our first rodeo people we just need you to be authentic and real and say we're sorry we'll fix it but there's another way and I'll leave you with this this is what I found to let ourselves be seen deeply sing voice thing to love with our whole hearts even though there's no guarantee and that's really hard and I can tell you the parent that's excruciating Lee difficult ,to practice gratitude and joy and those moments of kind of Terror when we were wondering can I love you this much can I believe in this is passionately can I be this Fierce about this just to be able to stop and instead of catastrophizing what might happen to say I'm just so grateful because I feel this wonderful means I'm alive and the last which I think is probably the most important it's a believe that were enough because when we work from a place I believe that says I'm enough then we stop screaming and start listening for Kinder and gentler to the people around us then we're Kinder and gentler Char South that's all I have ,that was brene brown recorded at tedx Houston in Houston Texas June 2010 for more information on Ted visit ted.com ,",
                    "beginOffset": -1
                },
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": 0.20000000298023224
                }
            }
        ],
        "entities": [
            {
                "name": "street fight",
                "type": "OTHER",
                "salience": 0.495470255613327,
                "mentions": [
                    {
                        "text": {
                            "content": "idea",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    },
                    {
                        "text": {
                            "content": "chance",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": 0.4000000059604645
                        }
                    },
                    {
                        "text": {
                            "content": "part",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "street fight",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "believe",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 39,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "researcher",
                "type": "PERSON",
                "salience": 0.20164872705936432,
                "mentions": [
                    {
                        "text": {
                            "content": "researcher",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    },
                    {
                        "text": {
                            "content": "student",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "researcher storyteller",
                "type": "PERSON",
                "salience": 0.17270593345165253,
                "mentions": [
                    {
                        "text": {
                            "content": "Storyteller",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "Storyteller",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    },
                    {
                        "text": {
                            "content": "researcher storyteller",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "Storyteller",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "researcher",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 5,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "way",
                "type": "OTHER",
                "salience": 0.008243506774306297,
                "mentions": [
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "something",
                "type": "OTHER",
                "salience": 0.007390607614070177,
                "mentions": [
                    {
                        "text": {
                            "content": "something",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    },
                    {
                        "text": {
                            "content": "something",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    },
                    {
                        "text": {
                            "content": "something",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "something",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "something",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "something",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1.899999976158142,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "brene Brown",
                "type": "PERSON",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Brené_Brown",
                    "mid": "/m/0dgnsl1"
                },
                "salience": 0.00508237536996603,
                "mentions": [
                    {
                        "text": {
                            "content": "brene Brown",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    },
                    {
                        "text": {
                            "content": "brene Brown",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 2.9000000953674316,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "struggle",
                "type": "OTHER",
                "salience": 0.004794343374669552,
                "mentions": [
                    {
                        "text": {
                            "content": "struggle",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1.5,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "stories",
                "type": "OTHER",
                "salience": 0.004721757024526596,
                "mentions": [
                    {
                        "text": {
                            "content": "stories",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    },
                    {
                        "text": {
                            "content": "data",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "story",
                "type": "OTHER",
                "salience": 0.0034700948745012283,
                "mentions": [
                    {
                        "text": {
                            "content": "story",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.0030436282977461815,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.002556109568104148,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "mantra",
                "type": "OTHER",
                "salience": 0.0024971042294055223,
                "mentions": [
                    {
                        "text": {
                            "content": "mantra",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "TED Talks",
                "type": "ORGANIZATION",
                "metadata": {
                    "mid": "/m/058p1b",
                    "wikipedia_url": "https://en.wikipedia.org/wiki/TED_(conference)"
                },
                "salience": 0.002451630774885416,
                "mentions": [
                    {
                        "text": {
                            "content": "TED Talks",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "Ted conference",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "Ted",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    },
                    {
                        "text": {
                            "content": "ted.com",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "most",
                "type": "PERSON",
                "salience": 0.0022075201850384474,
                "mentions": [
                    {
                        "text": {
                            "content": "most",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 10.600000381469727,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.0021005249582231045,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "opportunity",
                "type": "OTHER",
                "salience": 0.002018073108047247,
                "mentions": [
                    {
                        "text": {
                            "content": "situation",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "opportunity",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896
                }
            },
            {
                "name": "research Professor",
                "type": "PERSON",
                "salience": 0.0018445018213242292,
                "mentions": [
                    {
                        "text": {
                            "content": "research Professor",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "pattern",
                "type": "OTHER",
                "salience": 0.001727654249407351,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    },
                    {
                        "text": {
                            "content": "pattern",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "episode",
                "type": "WORK_OF_ART",
                "salience": 0.0016256383387371898,
                "mentions": [
                    {
                        "text": {
                            "content": "episode",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.0013810609234496951,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "love",
                "type": "OTHER",
                "salience": 0.0012197905452921987,
                "mentions": [
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    },
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    },
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    },
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    },
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "way",
                "type": "OTHER",
                "salience": 0.001171611249446869,
                "mentions": [
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.0011611091904342175,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "researcher",
                "type": "PERSON",
                "salience": 0.0011542290449142456,
                "mentions": [
                    {
                        "text": {
                            "content": "researcher",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.0011542290449142456,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "things",
                "type": "OTHER",
                "salience": 0.0011449994053691626,
                "mentions": [
                    {
                        "text": {
                            "content": "things",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612
                }
            },
            {
                "name": "Storyteller",
                "type": "PERSON",
                "salience": 0.0011333351721987128,
                "mentions": [
                    {
                        "text": {
                            "content": "Storyteller",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 11.399999618530273,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "Storyteller",
                "type": "PERSON",
                "salience": 0.0011333351721987128,
                "mentions": [
                    {
                        "text": {
                            "content": "Storyteller",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.0011263081105425954,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "queer",
                "type": "OTHER",
                "salience": 0.0010818849550560117,
                "mentions": [
                    {
                        "text": {
                            "content": "queer",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "ability",
                "type": "OTHER",
                "salience": 0.0010595099302008748,
                "mentions": [
                    {
                        "text": {
                            "content": "ability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.0010146652348339558,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "things",
                "type": "OTHER",
                "salience": 0.0009639483760111034,
                "mentions": [
                    {
                        "text": {
                            "content": "things",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "perception",
                "type": "OTHER",
                "salience": 0.0009588162647560239,
                "mentions": [
                    {
                        "text": {
                            "content": "perception",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "therapist",
                "type": "PERSON",
                "salience": 0.0009498896542936563,
                "mentions": [
                    {
                        "text": {
                            "content": "therapist",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "event",
                "type": "EVENT",
                "salience": 0.0009014307288452983,
                "mentions": [
                    {
                        "text": {
                            "content": "event",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "courage",
                "type": "OTHER",
                "salience": 0.0008906519506126642,
                "mentions": [
                    {
                        "text": {
                            "content": "courage",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "course",
                "type": "OTHER",
                "salience": 0.0008906519506126642,
                "mentions": [
                    {
                        "text": {
                            "content": "course",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.0008795922040008008,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "part",
                "type": "OTHER",
                "salience": 0.0008666631183587015,
                "mentions": [
                    {
                        "text": {
                            "content": "part",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.000861465698108077,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "partner",
                "type": "PERSON",
                "salience": 0.0007663607830181718,
                "mentions": [
                    {
                        "text": {
                            "content": "partner",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "events",
                "type": "EVENT",
                "salience": 0.0007135720225051045,
                "mentions": [
                    {
                        "text": {
                            "content": "events",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "talk",
                "type": "OTHER",
                "salience": 0.0007135720225051045,
                "mentions": [
                    {
                        "text": {
                            "content": "talk",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "story",
                "type": "OTHER",
                "salience": 0.0007042124634608626,
                "mentions": [
                    {
                        "text": {
                            "content": "story",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.0006998426979407668,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.0006845348398201168,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.0006720140227116644,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "Social Work",
                "type": "OTHER",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Social_work",
                    "mid": "/m/012qgt"
                },
                "salience": 0.0006583891226910055,
                "mentions": [
                    {
                        "text": {
                            "content": "Social Work",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    },
                    {
                        "text": {
                            "content": "Social Work",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "no one",
                "type": "PERSON",
                "salience": 0.0006508389487862587,
                "mentions": [
                    {
                        "text": {
                            "content": "no one",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "professor",
                "type": "PERSON",
                "salience": 0.000604522239882499,
                "mentions": [
                    {
                        "text": {
                            "content": "professor",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "flyer",
                "type": "OTHER",
                "salience": 0.000571662443690002,
                "mentions": [
                    {
                        "text": {
                            "content": "flyer",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "magic pixie",
                "type": "OTHER",
                "salience": 0.000571662443690002,
                "mentions": [
                    {
                        "text": {
                            "content": "magic pixie",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "second",
                "type": "OTHER",
                "salience": 0.000571662443690002,
                "mentions": [
                    {
                        "text": {
                            "content": "second",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "event planner",
                "type": "OTHER",
                "salience": 0.000571662443690002,
                "mentions": [
                    {
                        "text": {
                            "content": "event planner",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "soul",
                "type": "OTHER",
                "salience": 0.000571662443690002,
                "mentions": [
                    {
                        "text": {
                            "content": "soul",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.0005573608796112239,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.0005538985133171082,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.0004805241187568754,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "social work",
                "type": "OTHER",
                "salience": 0.00047314580297097564,
                "mentions": [
                    {
                        "text": {
                            "content": "social work",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "work",
                "type": "OTHER",
                "salience": 0.00047314580297097564,
                "mentions": [
                    {
                        "text": {
                            "content": "work",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "social work",
                "type": "OTHER",
                "salience": 0.00047314580297097564,
                "mentions": [
                    {
                        "text": {
                            "content": "social work",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "brown",
                "type": "OTHER",
                "salience": 0.00045930512715131044,
                "mentions": [
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "brown",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "career",
                "type": "OTHER",
                "salience": 0.000447159050963819,
                "mentions": [
                    {
                        "text": {
                            "content": "career",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00044195001828484237,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.00042303974623791873,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00040546595118939877,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "stories",
                "type": "WORK_OF_ART",
                "salience": 0.0004047679540235549,
                "mentions": [
                    {
                        "text": {
                            "content": "stories",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "variable",
                "type": "OTHER",
                "salience": 0.0003934558480978012,
                "mentions": [
                    {
                        "text": {
                            "content": "variable",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00039076621760614216,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": 0.20000000298023224
                }
            },
            {
                "name": "husband",
                "type": "PERSON",
                "salience": 0.0003877472772728652,
                "mentions": [
                    {
                        "text": {
                            "content": "husband",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    },
                    {
                        "text": {
                            "content": "husband",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1.2000000476837158,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "folks",
                "type": "PERSON",
                "salience": 0.00038399090408347547,
                "mentions": [
                    {
                        "text": {
                            "content": "folks",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.0003633860615082085,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "life",
                "type": "OTHER",
                "salience": 0.0003551378904376179,
                "mentions": [
                    {
                        "text": {
                            "content": "life",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "Devon",
                "type": "LOCATION",
                "salience": 0.0003378292894922197,
                "mentions": [
                    {
                        "text": {
                            "content": "Devon",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "career",
                "type": "OTHER",
                "salience": 0.00031217883224599063,
                "mentions": [
                    {
                        "text": {
                            "content": "career",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "perception",
                "type": "OTHER",
                "salience": 0.00031217883224599063,
                "mentions": [
                    {
                        "text": {
                            "content": "perception",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "parent",
                "type": "PERSON",
                "salience": 0.00031217883224599063,
                "mentions": [
                    {
                        "text": {
                            "content": "parent",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "piece",
                "type": "WORK_OF_ART",
                "salience": 0.00031217883224599063,
                "mentions": [
                    {
                        "text": {
                            "content": "piece",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "human empathy",
                "type": "OTHER",
                "salience": 0.00030534571851603687,
                "mentions": [
                    {
                        "text": {
                            "content": "human empathy",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "sense",
                "type": "OTHER",
                "salience": 0.0002975984534714371,
                "mentions": [
                    {
                        "text": {
                            "content": "sense",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00028868569643236697,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": 0.20000000298023224
                }
            },
            {
                "name": "masters",
                "type": "PERSON",
                "salience": 0.0002741806674748659,
                "mentions": [
                    {
                        "text": {
                            "content": "masters",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "PHD",
                "type": "OTHER",
                "salience": 0.0002741806674748659,
                "mentions": [
                    {
                        "text": {
                            "content": "PHD",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "Bachelors",
                "type": "OTHER",
                "salience": 0.000270825665211305,
                "mentions": [
                    {
                        "text": {
                            "content": "Bachelors",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "job",
                "type": "OTHER",
                "salience": 0.00026468627038411796,
                "mentions": [
                    {
                        "text": {
                            "content": "job",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "job",
                "type": "OTHER",
                "salience": 0.00026197193074040115,
                "mentions": [
                    {
                        "text": {
                            "content": "job",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    },
                    {
                        "text": {
                            "content": "job",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    },
                    {
                        "text": {
                            "content": "job",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "things",
                "type": "OTHER",
                "salience": 0.00025951681891456246,
                "mentions": [
                    {
                        "text": {
                            "content": "things",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.00025911920238286257,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.00024728605058044195,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "work",
                "type": "OTHER",
                "salience": 0.00023921004321891814,
                "mentions": [
                    {
                        "text": {
                            "content": "work",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "words",
                "type": "OTHER",
                "salience": 0.00023546120792161673,
                "mentions": [
                    {
                        "text": {
                            "content": "words",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00023361426428891718,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00023361426428891718,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "order",
                "type": "OTHER",
                "salience": 0.00022335273388307542,
                "mentions": [
                    {
                        "text": {
                            "content": "order",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "folks",
                "type": "PERSON",
                "salience": 0.0002227140066679567,
                "mentions": [
                    {
                        "text": {
                            "content": "folks",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1.100000023841858,
                    "score": -0.5
                }
            },
            {
                "name": "worker",
                "type": "PERSON",
                "salience": 0.00021411753550637513,
                "mentions": [
                    {
                        "text": {
                            "content": "worker",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.00020766940724570304,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "slugfest",
                "type": "EVENT",
                "salience": 0.00020566524472087622,
                "mentions": [
                    {
                        "text": {
                            "content": "slugfest",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "stories",
                "type": "WORK_OF_ART",
                "salience": 0.00020390376448631287,
                "mentions": [
                    {
                        "text": {
                            "content": "stories",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "one",
                "type": "OTHER",
                "salience": 0.00020179922285024077,
                "mentions": [
                    {
                        "text": {
                            "content": "one",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "disappointment",
                "type": "OTHER",
                "salience": 0.00019585475092753768,
                "mentions": [
                    {
                        "text": {
                            "content": "grief",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    },
                    {
                        "text": {
                            "content": "disappointment",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.0001953403407242149,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    },
                    {
                        "text": {
                            "content": "kind",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "therapist",
                "type": "PERSON",
                "salience": 0.0001953085302375257,
                "mentions": [
                    {
                        "text": {
                            "content": "therapist",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00019229500321671367,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00019229500321671367,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00019229500321671367,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "life",
                "type": "OTHER",
                "salience": 0.0001918857597047463,
                "mentions": [
                    {
                        "text": {
                            "content": "life",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00019161502132192254,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "work",
                "type": "OTHER",
                "salience": 0.00017889744776766747,
                "mentions": [
                    {
                        "text": {
                            "content": "work",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "social work",
                "type": "OTHER",
                "salience": 0.00017889744776766747,
                "mentions": [
                    {
                        "text": {
                            "content": "social work",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "way",
                "type": "OTHER",
                "salience": 0.0001735208061290905,
                "mentions": [
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "love",
                "type": "OTHER",
                "salience": 0.00016776499978732318,
                "mentions": [
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": 0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": 0.4000000059604645
                }
            },
            {
                "name": "all",
                "type": "OTHER",
                "salience": 0.00016692942881491035,
                "mentions": [
                    {
                        "text": {
                            "content": "all",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "relationship",
                "type": "OTHER",
                "salience": 0.00016307867190334946,
                "mentions": [
                    {
                        "text": {
                            "content": "relationship",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.0001586900616530329,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00015838909894227982,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00015710017760284245,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.800000011920929,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.0001529344153823331,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "struggle",
                "type": "OTHER",
                "salience": 0.00015260385407600552,
                "mentions": [
                    {
                        "text": {
                            "content": "struggle",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    },
                    {
                        "text": {
                            "content": "struggle",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "story",
                "type": "OTHER",
                "salience": 0.00015068896755110472,
                "mentions": [
                    {
                        "text": {
                            "content": "story",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "opportunity",
                "type": "OTHER",
                "salience": 0.00014838286733720452,
                "mentions": [
                    {
                        "text": {
                            "content": "opportunity",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896
                }
            },
            {
                "name": "therapist",
                "type": "PERSON",
                "salience": 0.00014825706603005528,
                "mentions": [
                    {
                        "text": {
                            "content": "therapist",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.00014792011643294245,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "discomfort",
                "type": "OTHER",
                "salience": 0.00014734003343619406,
                "mentions": [
                    {
                        "text": {
                            "content": "discomfort",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "hack",
                "type": "OTHER",
                "salience": 0.00014720030594617128,
                "mentions": [
                    {
                        "text": {
                            "content": "hack",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "things",
                "type": "OTHER",
                "salience": 0.00014712009578943253,
                "mentions": [
                    {
                        "text": {
                            "content": "things",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "anyone",
                "type": "PERSON",
                "salience": 0.00014704266504850239,
                "mentions": [
                    {
                        "text": {
                            "content": "anyone",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "things",
                "type": "OTHER",
                "salience": 0.00014671636745333672,
                "mentions": [
                    {
                        "text": {
                            "content": "things",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612
                }
            },
            {
                "name": "disconnection",
                "type": "OTHER",
                "salience": 0.0001460876956116408,
                "mentions": [
                    {
                        "text": {
                            "content": "disconnection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00014530746557284147,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.0001410640252288431,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.0001400349719915539,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.0001396506850142032,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.00013872150157112628,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.00013828385272063315,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "heartbreak",
                "type": "OTHER",
                "salience": 0.00013780368317384273,
                "mentions": [
                    {
                        "text": {
                            "content": "heartbreak",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "stories",
                "type": "WORK_OF_ART",
                "salience": 0.0001371181133436039,
                "mentions": [
                    {
                        "text": {
                            "content": "stories",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "stories",
                "type": "OTHER",
                "salience": 0.0001371181133436039,
                "mentions": [
                    {
                        "text": {
                            "content": "stories",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.0001345492637483403,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "kind",
                "type": "OTHER",
                "salience": 0.00013389003288466483,
                "mentions": [
                    {
                        "text": {
                            "content": "kind",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "evaluation",
                "type": "OTHER",
                "salience": 0.00013193185441195965,
                "mentions": [
                    {
                        "text": {
                            "content": "evaluation",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "kind",
                "type": "OTHER",
                "salience": 0.00013063257210887969,
                "mentions": [
                    {
                        "text": {
                            "content": "kind",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00013015751028433442,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00013015751028433442,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00012920799781568348,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.00012895528925582767,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00012885341129731387,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "lives",
                "type": "OTHER",
                "salience": 0.00012875662650913,
                "mentions": [
                    {
                        "text": {
                            "content": "lives",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "all",
                "type": "OTHER",
                "salience": 0.0001246854371856898,
                "mentions": [
                    {
                        "text": {
                            "content": "all",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.00012264780525583774,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.00012264780525583774,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "Char South",
                "type": "ORGANIZATION",
                "salience": 0.0001224055449711159,
                "mentions": [
                    {
                        "text": {
                            "content": "Char South",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.00012226085527800024,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "stories",
                "type": "WORK_OF_ART",
                "salience": 0.000120728844194673,
                "mentions": [
                    {
                        "text": {
                            "content": "stories",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "work",
                "type": "OTHER",
                "salience": 0.00011927788000321016,
                "mentions": [
                    {
                        "text": {
                            "content": "work",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.0001191805858979933,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.800000011920929,
                            "score": -0.800000011920929
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.800000011920929,
                    "score": -0.800000011920929
                }
            },
            {
                "name": "connection",
                "type": "OTHER",
                "salience": 0.00011898476077476516,
                "mentions": [
                    {
                        "text": {
                            "content": "connection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "more",
                "type": "OTHER",
                "salience": 0.00011801387881860137,
                "mentions": [
                    {
                        "text": {
                            "content": "more",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "growth",
                "type": "OTHER",
                "salience": 0.00011742604692699388,
                "mentions": [
                    {
                        "text": {
                            "content": "growth",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "growth",
                "type": "OTHER",
                "salience": 0.00011742604692699388,
                "mentions": [
                    {
                        "text": {
                            "content": "growth",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "therapist",
                "type": "PERSON",
                "salience": 0.000117326489998959,
                "mentions": [
                    {
                        "text": {
                            "content": "therapist",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.00011325432569719851,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "fear",
                "type": "OTHER",
                "salience": 0.00011259442544542253,
                "mentions": [
                    {
                        "text": {
                            "content": "fear",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "part",
                "type": "OTHER",
                "salience": 0.00011259442544542253,
                "mentions": [
                    {
                        "text": {
                            "content": "part",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.00011185468611074612,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.00011185468611074612,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "one",
                "type": "PERSON",
                "salience": 0.00011185468611074612,
                "mentions": [
                    {
                        "text": {
                            "content": "one",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "fear",
                "type": "OTHER",
                "salience": 0.0001117730134865269,
                "mentions": [
                    {
                        "text": {
                            "content": "fear",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00010885698429774493,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "belonging",
                "type": "OTHER",
                "salience": 0.00010880485933739692,
                "mentions": [
                    {
                        "text": {
                            "content": "belonging",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": 0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": 0.5
                }
            },
            {
                "name": "belonging",
                "type": "OTHER",
                "salience": 0.00010880485933739692,
                "mentions": [
                    {
                        "text": {
                            "content": "belonging",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "courage",
                "type": "OTHER",
                "salience": 0.00010859849135158584,
                "mentions": [
                    {
                        "text": {
                            "content": "courage",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "kind",
                "type": "OTHER",
                "salience": 0.00010859849135158584,
                "mentions": [
                    {
                        "text": {
                            "content": "kind",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "courage",
                "type": "OTHER",
                "salience": 0.00010859849135158584,
                "mentions": [
                    {
                        "text": {
                            "content": "courage",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "courage",
                "type": "OTHER",
                "salience": 0.00010859849135158584,
                "mentions": [
                    {
                        "text": {
                            "content": "courage",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "courage",
                "type": "OTHER",
                "salience": 0.00010859849135158584,
                "mentions": [
                    {
                        "text": {
                            "content": "courage",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "effect",
                "type": "OTHER",
                "salience": 0.00010664870933396742,
                "mentions": [
                    {
                        "text": {
                            "content": "effect",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "saying",
                "type": "OTHER",
                "salience": 0.0001036448375089094,
                "mentions": [
                    {
                        "text": {
                            "content": "saying",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "head",
                "type": "OTHER",
                "salience": 0.0001036448375089094,
                "mentions": [
                    {
                        "text": {
                            "content": "head",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "all",
                "type": "OTHER",
                "salience": 0.00010328768257750198,
                "mentions": [
                    {
                        "text": {
                            "content": "all",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.00010328768257750198,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "topics",
                "type": "OTHER",
                "salience": 0.0001031285646604374,
                "mentions": [
                    {
                        "text": {
                            "content": "topics",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "boss",
                "type": "PERSON",
                "salience": 0.0001031285646604374,
                "mentions": [
                    {
                        "text": {
                            "content": "boss",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "justice",
                "type": "OTHER",
                "salience": 0.0001031285646604374,
                "mentions": [
                    {
                        "text": {
                            "content": "justice",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "abuse",
                "type": "OTHER",
                "salience": 0.0001031285646604374,
                "mentions": [
                    {
                        "text": {
                            "content": "abuse",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "mental health",
                "type": "OTHER",
                "salience": 0.0001031285646604374,
                "mentions": [
                    {
                        "text": {
                            "content": "mental health",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "willingness",
                "type": "OTHER",
                "salience": 0.00010067019320558757,
                "mentions": [
                    {
                        "text": {
                            "content": "willingness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "somebody",
                "type": "PERSON",
                "salience": 0.00009939682058757171,
                "mentions": [
                    {
                        "text": {
                            "content": "somebody",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "sense",
                "type": "OTHER",
                "salience": 0.00009904149919748306,
                "mentions": [
                    {
                        "text": {
                            "content": "sense",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "disconnection",
                "type": "OTHER",
                "salience": 0.00009850578499026597,
                "mentions": [
                    {
                        "text": {
                            "content": "disconnection",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "sense",
                "type": "OTHER",
                "salience": 0.00009801510168472305,
                "mentions": [
                    {
                        "text": {
                            "content": "sense",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "sense",
                "type": "OTHER",
                "salience": 0.00009801510168472305,
                "mentions": [
                    {
                        "text": {
                            "content": "sense",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": 0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": 0.8999999761581421
                }
            },
            {
                "name": "sense",
                "type": "OTHER",
                "salience": 0.00009801510168472305,
                "mentions": [
                    {
                        "text": {
                            "content": "sense",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": 0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": 0.8999999761581421
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00009714676707517356,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1.2000000476837158,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.00009666140249464661,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "definition",
                "type": "OTHER",
                "salience": 0.00009583100472809747,
                "mentions": [
                    {
                        "text": {
                            "content": "definition",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "therapist",
                "type": "PERSON",
                "salience": 0.00009530136594548821,
                "mentions": [
                    {
                        "text": {
                            "content": "therapist",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "everyone",
                "type": "PERSON",
                "salience": 0.00009520751336822286,
                "mentions": [
                    {
                        "text": {
                            "content": "everyone",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "way",
                "type": "OTHER",
                "salience": 0.00009514666453469545,
                "mentions": [
                    {
                        "text": {
                            "content": "way",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "interviews",
                "type": "WORK_OF_ART",
                "salience": 0.00009360235708300024,
                "mentions": [
                    {
                        "text": {
                            "content": "interviews",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "heart",
                "type": "OTHER",
                "salience": 0.00009342481644125655,
                "mentions": [
                    {
                        "text": {
                            "content": "heart",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "heart",
                "type": "OTHER",
                "salience": 0.00009342481644125655,
                "mentions": [
                    {
                        "text": {
                            "content": "heart",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "internet",
                "type": "OTHER",
                "salience": 0.00009342481644125655,
                "mentions": [
                    {
                        "text": {
                            "content": "internet",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "data",
                "type": "OTHER",
                "salience": 0.00009342481644125655,
                "mentions": [
                    {
                        "text": {
                            "content": "data",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "job",
                "type": "OTHER",
                "salience": 0.00009298258373746648,
                "mentions": [
                    {
                        "text": {
                            "content": "job",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "data",
                "type": "OTHER",
                "salience": 0.00009266446431865916,
                "mentions": [
                    {
                        "text": {
                            "content": "data",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "bone ability",
                "type": "OTHER",
                "salience": 0.00009266446431865916,
                "mentions": [
                    {
                        "text": {
                            "content": "bone ability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.0000918601726880297,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "purpose",
                "type": "OTHER",
                "salience": 0.00008955578232416883,
                "mentions": [
                    {
                        "text": {
                            "content": "purpose",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "religion",
                "type": "OTHER",
                "salience": 0.00008853762847138569,
                "mentions": [
                    {
                        "text": {
                            "content": "religion",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "book",
                "type": "WORK_OF_ART",
                "salience": 0.0000873198441695422,
                "mentions": [
                    {
                        "text": {
                            "content": "book",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "talk",
                "type": "OTHER",
                "salience": 0.00008714741125004366,
                "mentions": [
                    {
                        "text": {
                            "content": "talk",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "definition",
                "type": "OTHER",
                "salience": 0.00008698211604496464,
                "mentions": [
                    {
                        "text": {
                            "content": "definition",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "definition",
                "type": "OTHER",
                "salience": 0.00008698211604496464,
                "mentions": [
                    {
                        "text": {
                            "content": "definition",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "folks",
                "type": "PERSON",
                "salience": 0.00008698211604496464,
                "mentions": [
                    {
                        "text": {
                            "content": "folks",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "compassion",
                "type": "OTHER",
                "salience": 0.00008698211604496464,
                "mentions": [
                    {
                        "text": {
                            "content": "compassion",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "worthiness",
                "type": "OTHER",
                "salience": 0.00008698211604496464,
                "mentions": [
                    {
                        "text": {
                            "content": "worthiness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "breakdown",
                "type": "EVENT",
                "salience": 0.00008671330579090863,
                "mentions": [
                    {
                        "text": {
                            "content": "breakdown",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "stuff",
                "type": "OTHER",
                "salience": 0.00008627418719697744,
                "mentions": [
                    {
                        "text": {
                            "content": "stuff",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "worthiness",
                "type": "OTHER",
                "salience": 0.00008608067582827061,
                "mentions": [
                    {
                        "text": {
                            "content": "worthiness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00008510276529705152,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": 0.20000000298023224
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.00008498279930790886,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.00008498279930790886,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 5,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "willingness",
                "type": "OTHER",
                "salience": 0.00008472626359434798,
                "mentions": [
                    {
                        "text": {
                            "content": "willingness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "original",
                "type": "WORK_OF_ART",
                "salience": 0.0000838043779367581,
                "mentions": [
                    {
                        "text": {
                            "content": "original",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "list",
                "type": "OTHER",
                "salience": 0.00008354538294952363,
                "mentions": [
                    {
                        "text": {
                            "content": "list",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": 0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": 0.10000000149011612
                }
            },
            {
                "name": "last",
                "type": "OTHER",
                "salience": 0.00008231302490457892,
                "mentions": [
                    {
                        "text": {
                            "content": "last",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "discourse",
                "type": "OTHER",
                "salience": 0.00008179038559319451,
                "mentions": [
                    {
                        "text": {
                            "content": "discourse",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "interviews",
                "type": "EVENT",
                "salience": 0.00008158779382938519,
                "mentions": [
                    {
                        "text": {
                            "content": "interviews",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "compassion",
                "type": "OTHER",
                "salience": 0.00007979725342011079,
                "mentions": [
                    {
                        "text": {
                            "content": "compassion",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "breakdown",
                "type": "EVENT",
                "salience": 0.00007966612611198798,
                "mentions": [
                    {
                        "text": {
                            "content": "breakdown",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "break",
                "type": "EVENT",
                "salience": 0.00007966612611198798,
                "mentions": [
                    {
                        "text": {
                            "content": "break",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "willingness",
                "type": "OTHER",
                "salience": 0.00007966612611198798,
                "mentions": [
                    {
                        "text": {
                            "content": "willingness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "reason",
                "type": "OTHER",
                "salience": 0.00007966612611198798,
                "mentions": [
                    {
                        "text": {
                            "content": "reason",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "reason",
                "type": "OTHER",
                "salience": 0.00007966612611198798,
                "mentions": [
                    {
                        "text": {
                            "content": "reason",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "live",
                "type": "OTHER",
                "salience": 0.00007955064211273566,
                "mentions": [
                    {
                        "text": {
                            "content": "live",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "notebook manila folder",
                "type": "OTHER",
                "salience": 0.00007947790436446667,
                "mentions": [
                    {
                        "text": {
                            "content": "notebook manila folder",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "word",
                "type": "OTHER",
                "salience": 0.0000793271537986584,
                "mentions": [
                    {
                        "text": {
                            "content": "word",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "manila folder",
                "type": "OTHER",
                "salience": 0.0000793271537986584,
                "mentions": [
                    {
                        "text": {
                            "content": "manila folder",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "kids",
                "type": "PERSON",
                "salience": 0.0000793271537986584,
                "mentions": [
                    {
                        "text": {
                            "content": "kids",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "feeling",
                "type": "OTHER",
                "salience": 0.00007889806147431955,
                "mentions": [
                    {
                        "text": {
                            "content": "feeling",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "no one",
                "type": "PERSON",
                "salience": 0.00007889806147431955,
                "mentions": [
                    {
                        "text": {
                            "content": "no one",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "thousands",
                "type": "PERSON",
                "salience": 0.00007868152169976383,
                "mentions": [
                    {
                        "text": {
                            "content": "thousands",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "pieces",
                "type": "WORK_OF_ART",
                "salience": 0.00007868152169976383,
                "mentions": [
                    {
                        "text": {
                            "content": "pieces",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "order",
                "type": "OTHER",
                "salience": 0.00007868152169976383,
                "mentions": [
                    {
                        "text": {
                            "content": "order",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "stick",
                "type": "CONSUMER_GOOD",
                "salience": 0.00007868152169976383,
                "mentions": [
                    {
                        "text": {
                            "content": "stick",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "office supply addiction",
                "type": "OTHER",
                "salience": 0.0000785050360718742,
                "mentions": [
                    {
                        "text": {
                            "content": "office supply addiction",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "someone",
                "type": "PERSON",
                "salience": 0.00007750376244075596,
                "mentions": [
                    {
                        "text": {
                            "content": "someone",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "one",
                "type": "OTHER",
                "salience": 0.00007750376244075596,
                "mentions": [
                    {
                        "text": {
                            "content": "one",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "experiences",
                "type": "OTHER",
                "salience": 0.00007646608719369397,
                "mentions": [
                    {
                        "text": {
                            "content": "experiences",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00007600602839374915,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00007593668124172837,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00007593668124172837,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1,
                    "score": -0.5
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00007422979979310185,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "Shane",
                "type": "PERSON",
                "salience": 0.00007341887248912826,
                "mentions": [
                    {
                        "text": {
                            "content": "Shane",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    },
                    {
                        "text": {
                            "content": "Shane",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "control",
                "type": "OTHER",
                "salience": 0.00007265492604346946,
                "mentions": [
                    {
                        "text": {
                            "content": "control",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "doctor",
                "type": "PERSON",
                "salience": 0.00007265492604346946,
                "mentions": [
                    {
                        "text": {
                            "content": "doctor",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "control",
                "type": "OTHER",
                "salience": 0.00007265492604346946,
                "mentions": [
                    {
                        "text": {
                            "content": "control",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "friends",
                "type": "PERSON",
                "salience": 0.00007254960655700415,
                "mentions": [
                    {
                        "text": {
                            "content": "friends",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "friends",
                "type": "PERSON",
                "salience": 0.00007254960655700415,
                "mentions": [
                    {
                        "text": {
                            "content": "friends",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "everyone",
                "type": "PERSON",
                "salience": 0.0000721738106221892,
                "mentions": [
                    {
                        "text": {
                            "content": "everyone",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "stuff",
                "type": "OTHER",
                "salience": 0.00007190825999714434,
                "mentions": [
                    {
                        "text": {
                            "content": "stuff",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "problem",
                "type": "OTHER",
                "salience": 0.00007190825999714434,
                "mentions": [
                    {
                        "text": {
                            "content": "problem",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "everything",
                "type": "OTHER",
                "salience": 0.00007183124398579821,
                "mentions": [
                    {
                        "text": {
                            "content": "everything",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "voice thing",
                "type": "OTHER",
                "salience": 0.00007091682346072048,
                "mentions": [
                    {
                        "text": {
                            "content": "voice thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "guarantees",
                "type": "OTHER",
                "salience": 0.00007088708662195131,
                "mentions": [
                    {
                        "text": {
                            "content": "guarantees",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "mind",
                "type": "OTHER",
                "salience": 0.00006980029866099358,
                "mentions": [
                    {
                        "text": {
                            "content": "mind",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "Sharpie",
                "type": "OTHER",
                "salience": 0.00006980029866099358,
                "mentions": [
                    {
                        "text": {
                            "content": "Sharpie",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "world",
                "type": "LOCATION",
                "salience": 0.00006974526331759989,
                "mentions": [
                    {
                        "text": {
                            "content": "world",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "data analysis",
                "type": "OTHER",
                "salience": 0.0000696679053362459,
                "mentions": [
                    {
                        "text": {
                            "content": "data analysis",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "language",
                "type": "OTHER",
                "salience": 0.0000696679053362459,
                "mentions": [
                    {
                        "text": {
                            "content": "language",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "bravery",
                "type": "OTHER",
                "salience": 0.0000696679053362459,
                "mentions": [
                    {
                        "text": {
                            "content": "bravery",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "researcher mode",
                "type": "OTHER",
                "salience": 0.0000696679053362459,
                "mentions": [
                    {
                        "text": {
                            "content": "researcher mode",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "riding",
                "type": "EVENT",
                "salience": 0.0000696679053362459,
                "mentions": [
                    {
                        "text": {
                            "content": "riding",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "top",
                "type": "OTHER",
                "salience": 0.0000696679053362459,
                "mentions": [
                    {
                        "text": {
                            "content": "top",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "fact",
                "type": "OTHER",
                "salience": 0.0000696679053362459,
                "mentions": [
                    {
                        "text": {
                            "content": "fact",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "mission",
                "type": "OTHER",
                "salience": 0.00006955341814318672,
                "mentions": [
                    {
                        "text": {
                            "content": "mission",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "fortune",
                "type": "OTHER",
                "salience": 0.00006929104711161926,
                "mentions": [
                    {
                        "text": {
                            "content": "fortune",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "pend",
                "type": "OTHER",
                "salience": 0.00006929104711161926,
                "mentions": [
                    {
                        "text": {
                            "content": "pend",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "pages",
                "type": "OTHER",
                "salience": 0.00006910087540745735,
                "mentions": [
                    {
                        "text": {
                            "content": "pages",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "interviews focus groups",
                "type": "ORGANIZATION",
                "salience": 0.00006910087540745735,
                "mentions": [
                    {
                        "text": {
                            "content": "interviews focus groups",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "theory",
                "type": "OTHER",
                "salience": 0.00006910087540745735,
                "mentions": [
                    {
                        "text": {
                            "content": "theory",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "scene",
                "type": "OTHER",
                "salience": 0.00006910087540745735,
                "mentions": [
                    {
                        "text": {
                            "content": "scene",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "capacity",
                "type": "OTHER",
                "salience": 0.00006844285962870345,
                "mentions": [
                    {
                        "text": {
                            "content": "capacity",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "more",
                "type": "OTHER",
                "salience": 0.00006799360562581569,
                "mentions": [
                    {
                        "text": {
                            "content": "more",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "discomfort",
                "type": "OTHER",
                "salience": 0.00006799360562581569,
                "mentions": [
                    {
                        "text": {
                            "content": "discomfort",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "code",
                "type": "OTHER",
                "salience": 0.00006784501601941884,
                "mentions": [
                    {
                        "text": {
                            "content": "code",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "addiction",
                "type": "OTHER",
                "salience": 0.00006714323535561562,
                "mentions": [
                    {
                        "text": {
                            "content": "addiction",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.800000011920929,
                            "score": -0.800000011920929
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.800000011920929,
                    "score": -0.800000011920929
                }
            },
            {
                "name": "evidence",
                "type": "OTHER",
                "salience": 0.0000655797339277342,
                "mentions": [
                    {
                        "text": {
                            "content": "evidence",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "fear",
                "type": "OTHER",
                "salience": 0.00006420622230507433,
                "mentions": [
                    {
                        "text": {
                            "content": "fear",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00006417494296329096,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "Courage",
                "type": "OTHER",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Courage",
                    "mid": "/m/0d7lc"
                },
                "salience": 0.00006415506504708901,
                "mentions": [
                    {
                        "text": {
                            "content": "Courage",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "result",
                "type": "OTHER",
                "salience": 0.00006391305214492604,
                "mentions": [
                    {
                        "text": {
                            "content": "result",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "authenticity",
                "type": "OTHER",
                "salience": 0.00006391305214492604,
                "mentions": [
                    {
                        "text": {
                            "content": "authenticity",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "others",
                "type": "PERSON",
                "salience": 0.00006391305214492604,
                "mentions": [
                    {
                        "text": {
                            "content": "others",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "phenomenon",
                "type": "OTHER",
                "salience": 0.0000638080236967653,
                "mentions": [
                    {
                        "text": {
                            "content": "phenomenon",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "lightning",
                "type": "OTHER",
                "salience": 0.0000638080236967653,
                "mentions": [
                    {
                        "text": {
                            "content": "lightning",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "awakening",
                "type": "OTHER",
                "salience": 0.0000638080236967653,
                "mentions": [
                    {
                        "text": {
                            "content": "awakening",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": 0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": 0.699999988079071
                }
            },
            {
                "name": "allegiance",
                "type": "OTHER",
                "salience": 0.0000638080236967653,
                "mentions": [
                    {
                        "text": {
                            "content": "allegiance",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "mammogram",
                "type": "OTHER",
                "salience": 0.0000638080236967653,
                "mentions": [
                    {
                        "text": {
                            "content": "mammogram",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "meeting",
                "type": "EVENT",
                "salience": 0.00006371552444761619,
                "mentions": [
                    {
                        "text": {
                            "content": "meeting",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "couple",
                "type": "PERSON",
                "salience": 0.00006342027336359024,
                "mentions": [
                    {
                        "text": {
                            "content": "couple",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "couple",
                "type": "PERSON",
                "salience": 0.00006335233774734661,
                "mentions": [
                    {
                        "text": {
                            "content": "couple",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "recommendations",
                "type": "OTHER",
                "salience": 0.0000629355781711638,
                "mentions": [
                    {
                        "text": {
                            "content": "recommendations",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "stick",
                "type": "CONSUMER_GOOD",
                "salience": 0.00006258162466110662,
                "mentions": [
                    {
                        "text": {
                            "content": "stick",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "life",
                "type": "OTHER",
                "salience": 0.00006257683708099648,
                "mentions": [
                    {
                        "text": {
                            "content": "life",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "cock",
                "type": "OTHER",
                "salience": 0.00006125262007117271,
                "mentions": [
                    {
                        "text": {
                            "content": "cock",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "Bento Box",
                "type": "CONSUMER_GOOD",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Bento",
                    "mid": "/m/012x5p"
                },
                "salience": 0.00006122844206402078,
                "mentions": [
                    {
                        "text": {
                            "content": "Bento Box",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "A",
                "type": "LOCATION",
                "salience": 0.000060923430282855406,
                "mentions": [
                    {
                        "text": {
                            "content": "A",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "job",
                "type": "OTHER",
                "salience": 0.00006012012454448268,
                "mentions": [
                    {
                        "text": {
                            "content": "job",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "reason",
                "type": "OTHER",
                "salience": 0.000059778256400022656,
                "mentions": [
                    {
                        "text": {
                            "content": "reason",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "lives",
                "type": "OTHER",
                "salience": 0.000059778256400022656,
                "mentions": [
                    {
                        "text": {
                            "content": "lives",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "emotion",
                "type": "OTHER",
                "salience": 0.000057594257668824866,
                "mentions": [
                    {
                        "text": {
                            "content": "emotion",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "conversation",
                "type": "OTHER",
                "salience": 0.00005753256846219301,
                "mentions": [
                    {
                        "text": {
                            "content": "conversation",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "fat",
                "type": "OTHER",
                "salience": 0.000054766784160165116,
                "mentions": [
                    {
                        "text": {
                            "content": "fat",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "gratitude",
                "type": "OTHER",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "gratitude",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "beers",
                "type": "CONSUMER_GOOD",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "beers",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "evidence",
                "type": "OTHER",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "evidence",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "feeling",
                "type": "OTHER",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "feeling",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "purpose",
                "type": "OTHER",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "purpose",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "world",
                "type": "LOCATION",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "world",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "doctor",
                "type": "PERSON",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "doctor",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "sex",
                "type": "OTHER",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "sex",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "banana nut muffin",
                "type": "OTHER",
                "salience": 0.00005451716424431652,
                "mentions": [
                    {
                        "text": {
                            "content": "banana nut muffin",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "banana nut muffin",
                "type": "OTHER",
                "salience": 0.00005445877104648389,
                "mentions": [
                    {
                        "text": {
                            "content": "banana nut muffin",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "beers",
                "type": "CONSUMER_GOOD",
                "salience": 0.00005445877104648389,
                "mentions": [
                    {
                        "text": {
                            "content": "beers",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "belief",
                "type": "OTHER",
                "salience": 0.00005445877104648389,
                "mentions": [
                    {
                        "text": {
                            "content": "belief",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "love",
                "type": "OTHER",
                "salience": 0.00005411367237684317,
                "mentions": [
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.00005371356746763922,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "kind",
                "type": "OTHER",
                "salience": 0.00005206304194871336,
                "mentions": [
                    {
                        "text": {
                            "content": "kind",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "Manila",
                "type": "LOCATION",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Manila",
                    "mid": "/m/0195pd"
                },
                "salience": 0.00005148191485204734,
                "mentions": [
                    {
                        "text": {
                            "content": "Manila",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "lot",
                "type": "OTHER",
                "salience": 0.00005141683141118847,
                "mentions": [
                    {
                        "text": {
                            "content": "lot",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "cycle",
                "type": "OTHER",
                "salience": 0.000050865375669673085,
                "mentions": [
                    {
                        "text": {
                            "content": "cycle",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "town",
                "type": "LOCATION",
                "salience": 0.00005057737143943086,
                "mentions": [
                    {
                        "text": {
                            "content": "town",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "Kinder",
                "type": "PERSON",
                "salience": 0.00005027094448450953,
                "mentions": [
                    {
                        "text": {
                            "content": "Kinder",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "Kinder",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "company",
                "type": "ORGANIZATION",
                "salience": 0.000050160891987616196,
                "mentions": [
                    {
                        "text": {
                            "content": "company",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224
                }
            },
            {
                "name": "handle",
                "type": "OTHER",
                "salience": 0.00004927291956846602,
                "mentions": [
                    {
                        "text": {
                            "content": "handle",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "cat",
                "type": "OTHER",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "cat",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "ways",
                "type": "OTHER",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "ways",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "meaning",
                "type": "OTHER",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "meaning",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "living",
                "type": "OTHER",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "living",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "debt",
                "type": "OTHER",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "debt",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "kitten",
                "type": "PERSON",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "kitten",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "wife",
                "type": "PERSON",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "wife",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "happiness",
                "type": "OTHER",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "happiness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "history",
                "type": "OTHER",
                "salience": 0.00004787863144883886,
                "mentions": [
                    {
                        "text": {
                            "content": "history",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "faith",
                "type": "OTHER",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "faith",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "certainty",
                "type": "OTHER",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "certainty",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "butt",
                "type": "OTHER",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "butt",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "mystery",
                "type": "OTHER",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "mystery",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "cheeks",
                "type": "OTHER",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "cheeks",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "pain",
                "type": "OTHER",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "pain",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "death",
                "type": "EVENT",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "death",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "blame",
                "type": "OTHER",
                "salience": 0.00004782734686159529,
                "mentions": [
                    {
                        "text": {
                            "content": "blame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "people",
                "type": "PERSON",
                "salience": 0.00004775141496793367,
                "mentions": [
                    {
                        "text": {
                            "content": "people",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "politics",
                "type": "OTHER",
                "salience": 0.00004666355744120665,
                "mentions": [
                    {
                        "text": {
                            "content": "politics",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "guarantee",
                "type": "OTHER",
                "salience": 0.0000457461537735071,
                "mentions": [
                    {
                        "text": {
                            "content": "guarantee",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "generation",
                "type": "PERSON",
                "salience": 0.00004548322249320336,
                "mentions": [
                    {
                        "text": {
                            "content": "generation",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "hearts",
                "type": "OTHER",
                "salience": 0.00004478800838114694,
                "mentions": [
                    {
                        "text": {
                            "content": "hearts",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "thing",
                "type": "OTHER",
                "salience": 0.00004465252277441323,
                "mentions": [
                    {
                        "text": {
                            "content": "thing",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "thousands",
                "type": "PERSON",
                "salience": 0.00004250280107953586,
                "mentions": [
                    {
                        "text": {
                            "content": "thousands",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "research",
                "type": "OTHER",
                "salience": 0.000042446612496860325,
                "mentions": [
                    {
                        "text": {
                            "content": "research",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "children",
                "type": "PERSON",
                "salience": 0.00004177835944574326,
                "mentions": [
                    {
                        "text": {
                            "content": "children",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "children",
                "type": "PERSON",
                "salience": 0.00004177835944574326,
                "mentions": [
                    {
                        "text": {
                            "content": "children",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "problems",
                "type": "OTHER",
                "salience": 0.00004173719207756221,
                "mentions": [
                    {
                        "text": {
                            "content": "problems",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "Fierce",
                "type": "OTHER",
                "salience": 0.00004117757634958252,
                "mentions": [
                    {
                        "text": {
                            "content": "Fierce",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "Cur",
                "type": "OTHER",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Cur",
                    "mid": "/m/02pfd6"
                },
                "salience": 0.00004115543924854137,
                "mentions": [
                    {
                        "text": {
                            "content": "Cur",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "Latin",
                "type": "OTHER",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Latin",
                    "mid": "/m/04h9h"
                },
                "salience": 0.00004115543924854137,
                "mentions": [
                    {
                        "text": {
                            "content": "Latin",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "English",
                "type": "OTHER",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/English_language",
                    "mid": "/m/02h40lc"
                },
                "salience": 0.00004115543924854137,
                "mentions": [
                    {
                        "text": {
                            "content": "English",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "Jackson Pollock",
                "type": "PERSON",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Jackson_Pollock",
                    "mid": "/m/04510"
                },
                "salience": 0.00004115543924854137,
                "mentions": [
                    {
                        "text": {
                            "content": "Jackson Pollock",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "hand",
                "type": "OTHER",
                "salience": 0.00003810133057413623,
                "mentions": [
                    {
                        "text": {
                            "content": "hand",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "seventh grade",
                "type": "OTHER",
                "salience": 0.000038063782994868234,
                "mentions": [
                    {
                        "text": {
                            "content": "seventh grade",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "kids",
                "type": "PERSON",
                "salience": 0.000038063782994868234,
                "mentions": [
                    {
                        "text": {
                            "content": "kids",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "grade",
                "type": "OTHER",
                "salience": 0.000038063782994868234,
                "mentions": [
                    {
                        "text": {
                            "content": "grade",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "last",
                "type": "OTHER",
                "salience": 0.000038029054849175736,
                "mentions": [
                    {
                        "text": {
                            "content": "last",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": 0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.800000011920929,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "gratitude",
                "type": "OTHER",
                "salience": 0.000038029054849175736,
                "mentions": [
                    {
                        "text": {
                            "content": "gratitude",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "joy",
                "type": "OTHER",
                "salience": 0.000038029054849175736,
                "mentions": [
                    {
                        "text": {
                            "content": "joy",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "Diana",
                "type": "PERSON",
                "salience": 0.00003763897984754294,
                "mentions": [
                    {
                        "text": {
                            "content": "Diana",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.000037277804949553683,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.000037277804949553683,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "vulnerability",
                "type": "OTHER",
                "salience": 0.00003637070403783582,
                "mentions": [
                    {
                        "text": {
                            "content": "vulnerability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "answer",
                "type": "OTHER",
                "salience": 0.00003446788832661696,
                "mentions": [
                    {
                        "text": {
                            "content": "answer",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "love",
                "type": "OTHER",
                "salience": 0.00003404100425541401,
                "mentions": [
                    {
                        "text": {
                            "content": "love",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": 0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": 0.10000000149011612
                }
            },
            {
                "name": "shame",
                "type": "OTHER",
                "salience": 0.00003404100425541401,
                "mentions": [
                    {
                        "text": {
                            "content": "shame",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "look",
                "type": "OTHER",
                "salience": 0.00003346162338857539,
                "mentions": [
                    {
                        "text": {
                            "content": "look",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "oil spill",
                "type": "EVENT",
                "salience": 0.00003342864874866791,
                "mentions": [
                    {
                        "text": {
                            "content": "oil spill",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "bail",
                "type": "OTHER",
                "salience": 0.00003342864874866791,
                "mentions": [
                    {
                        "text": {
                            "content": "bail",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "weather",
                "type": "OTHER",
                "salience": 0.00003342864874866791,
                "mentions": [
                    {
                        "text": {
                            "content": "weather",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "lies",
                "type": "OTHER",
                "salience": 0.00003342864874866791,
                "mentions": [
                    {
                        "text": {
                            "content": "lies",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "information",
                "type": "OTHER",
                "salience": 0.000033398147934349254,
                "mentions": [
                    {
                        "text": {
                            "content": "information",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "place",
                "type": "OTHER",
                "salience": 0.000033398147934349254,
                "mentions": [
                    {
                        "text": {
                            "content": "place",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "Terror",
                "type": "OTHER",
                "salience": 0.000033398147934349254,
                "mentions": [
                    {
                        "text": {
                            "content": "Terror",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": 0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": 0.4000000059604645
                }
            },
            {
                "name": "moments",
                "type": "OTHER",
                "salience": 0.000033398147934349254,
                "mentions": [
                    {
                        "text": {
                            "content": "moments",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": 0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": 0.6000000238418579
                }
            },
            {
                "name": "rodeo",
                "type": "OTHER",
                "salience": 0.000033398147934349254,
                "mentions": [
                    {
                        "text": {
                            "content": "rodeo",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "impact",
                "type": "OTHER",
                "salience": 0.00003298929732409306,
                "mentions": [
                    {
                        "text": {
                            "content": "impact",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "belonging",
                "type": "OTHER",
                "salience": 0.000032780888432171196,
                "mentions": [
                    {
                        "text": {
                            "content": "belonging",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "adult cohort",
                "type": "OTHER",
                "salience": 0.00003228229616070166,
                "mentions": [
                    {
                        "text": {
                            "content": "adult cohort",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "God",
                "type": "PERSON",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/God",
                    "mid": "/m/0d05l6"
                },
                "salience": 0.000032204963645199314,
                "mentions": [
                    {
                        "text": {
                            "content": "God",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "God",
                "type": "PERSON",
                "salience": 0.00003213843592675403,
                "mentions": [
                    {
                        "text": {
                            "content": "God",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "therapist",
                "type": "PERSON",
                "salience": 0.00003140861008432694,
                "mentions": [
                    {
                        "text": {
                            "content": "therapist",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "Lee",
                "type": "PERSON",
                "salience": 0.00003073865082114935,
                "mentions": [
                    {
                        "text": {
                            "content": "Lee",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.8999999761581421,
                            "score": -0.8999999761581421
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.8999999761581421
                }
            },
            {
                "name": "parent",
                "type": "PERSON",
                "salience": 0.00002829638651746791,
                "mentions": [
                    {
                        "text": {
                            "content": "parent",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "FXR",
                "type": "ORGANIZATION",
                "salience": 0.00002828323886205908,
                "mentions": [
                    {
                        "text": {
                            "content": "FXR",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "US",
                "type": "LOCATION",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/United_States",
                    "mid": "/m/09c7w0"
                },
                "salience": 0.00002828323886205908,
                "mentions": [
                    {
                        "text": {
                            "content": "US",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "fear",
                "type": "OTHER",
                "salience": 0.00002820010922732763,
                "mentions": [
                    {
                        "text": {
                            "content": "fear",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": -0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": -0.5
                }
            },
            {
                "name": "struggle",
                "type": "OTHER",
                "salience": 0.00002820010922732763,
                "mentions": [
                    {
                        "text": {
                            "content": "struggle",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.8999999761581421,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "ability",
                "type": "OTHER",
                "salience": 0.000028163536626379937,
                "mentions": [
                    {
                        "text": {
                            "content": "ability",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "life",
                "type": "OTHER",
                "salience": 0.000028163536626379937,
                "mentions": [
                    {
                        "text": {
                            "content": "life",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "babies",
                "type": "PERSON",
                "salience": 0.00002816149572026916,
                "mentions": [
                    {
                        "text": {
                            "content": "babies",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "tennis team",
                "type": "ORGANIZATION",
                "salience": 0.00002647943256306462,
                "mentions": [
                    {
                        "text": {
                            "content": "tennis team",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "worthiness",
                "type": "OTHER",
                "salience": 0.000026255176635459065,
                "mentions": [
                    {
                        "text": {
                            "content": "worthiness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "family stuff",
                "type": "OTHER",
                "salience": 0.000026255176635459065,
                "mentions": [
                    {
                        "text": {
                            "content": "family stuff",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "childhood",
                "type": "OTHER",
                "salience": 0.000026255176635459065,
                "mentions": [
                    {
                        "text": {
                            "content": "childhood",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "husband",
                "type": "PERSON",
                "salience": 0.000026190360586042516,
                "mentions": [
                    {
                        "text": {
                            "content": "husband",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 1.2000000476837158,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "Nam",
                "type": "LOCATION",
                "salience": 0.000025946766982087865,
                "mentions": [
                    {
                        "text": {
                            "content": "Nam",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.20000000298023224,
                            "score": -0.20000000298023224
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.20000000298023224,
                    "score": -0.20000000298023224
                }
            },
            {
                "name": "problem",
                "type": "OTHER",
                "salience": 0.000025933761207852513,
                "mentions": [
                    {
                        "text": {
                            "content": "problem",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "Houston",
                "type": "LOCATION",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Houston",
                    "mid": "/m/03l2n"
                },
                "salience": 0.000025375891709700227,
                "mentions": [
                    {
                        "text": {
                            "content": "Houston",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    },
                    {
                        "text": {
                            "content": "Houston",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "joy",
                "type": "OTHER",
                "salience": 0.000023944325221236795,
                "mentions": [
                    {
                        "text": {
                            "content": "joy",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": 0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": 0.4000000059604645
                }
            },
            {
                "name": "fight",
                "type": "EVENT",
                "salience": 0.00002391327143413946,
                "mentions": [
                    {
                        "text": {
                            "content": "fight",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "help",
                "type": "OTHER",
                "salience": 0.000023885213522589765,
                "mentions": [
                    {
                        "text": {
                            "content": "help",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "sex",
                "type": "OTHER",
                "salience": 0.000023885213522589765,
                "mentions": [
                    {
                        "text": {
                            "content": "sex",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "birthplace",
                "type": "LOCATION",
                "salience": 0.000022090522179496475,
                "mentions": [
                    {
                        "text": {
                            "content": "birthplace",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "decor",
                "type": "OTHER",
                "salience": 0.000021028490664320998,
                "mentions": [
                    {
                        "text": {
                            "content": "decor",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "creativity",
                "type": "OTHER",
                "salience": 0.000021028490664320998,
                "mentions": [
                    {
                        "text": {
                            "content": "creativity",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": -0.10000000149011612
                }
            },
            {
                "name": "surrender",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "surrender",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "responses",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "responses",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "half",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "half",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "call",
                "type": "EVENT",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "call",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "Mobility",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "Mobility",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.4000000059604645,
                            "score": -0.4000000059604645
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.4000000059604645,
                    "score": -0.4000000059604645
                }
            },
            {
                "name": "BI",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "B I",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "tenderness",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "tenderness",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.30000001192092896,
                            "score": -0.30000001192092896
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.30000001192092896,
                    "score": -0.30000001192092896
                }
            },
            {
                "name": "choices",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "choices",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "phone",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "phone",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "right",
                "type": "OTHER",
                "salience": 0.000021001218556193635,
                "mentions": [
                    {
                        "text": {
                            "content": "right",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.699999988079071,
                            "score": -0.699999988079071
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.699999988079071,
                    "score": -0.699999988079071
                }
            },
            {
                "name": "issue",
                "type": "OTHER",
                "salience": 0.00002077105818898417,
                "mentions": [
                    {
                        "text": {
                            "content": "issue",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": 0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": 0.6000000238418579
                }
            },
            {
                "name": "BS meters",
                "type": "OTHER",
                "salience": 0.000020516778022283688,
                "mentions": [
                    {
                        "text": {
                            "content": "BS meters",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.5,
                            "score": 0.5
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.5,
                    "score": 0.5
                }
            },
            {
                "name": "help",
                "type": "OTHER",
                "salience": 0.000020401383153512143,
                "mentions": [
                    {
                        "text": {
                            "content": "help",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "much",
                "type": "OTHER",
                "salience": 0.00002015561767620966,
                "mentions": [
                    {
                        "text": {
                            "content": "much",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": 0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": 0.10000000149011612
                }
            },
            {
                "name": "Texas",
                "type": "LOCATION",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Texas",
                    "mid": "/m/07b_l"
                },
                "salience": 0.000019729002815438434,
                "mentions": [
                    {
                        "text": {
                            "content": "Texas",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "strategy",
                "type": "OTHER",
                "salience": 0.000017916978322318755,
                "mentions": [
                    {
                        "text": {
                            "content": "strategy",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {}
                    }
                ],
                "sentiment": {}
            },
            {
                "name": "Adele",
                "type": "PERSON",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Adele",
                    "mid": "/m/02z4b_8"
                },
                "salience": 0.000012421864994394127,
                "mentions": [
                    {
                        "text": {
                            "content": "Adele",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {}
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612
                }
            },
            {
                "name": "II",
                "type": "LOCATION",
                "salience": 0.000012421864994394127,
                "mentions": [
                    {
                        "text": {
                            "content": "I I",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": 0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.10000000149011612,
                    "score": 0.10000000149011612
                }
            },
            {
                "name": "Facebook",
                "type": "OTHER",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Facebook",
                    "mid": "/m/02y1vz"
                },
                "salience": 0.000012405754205246922,
                "mentions": [
                    {
                        "text": {
                            "content": "Facebook",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "Twitter",
                "type": "OTHER",
                "metadata": {
                    "wikipedia_url": "https://en.wikipedia.org/wiki/Twitter",
                    "mid": "/m/0289n8t"
                },
                "salience": 0.000012405754205246922,
                "mentions": [
                    {
                        "text": {
                            "content": "Twitter",
                            "beginOffset": -1
                        },
                        "type": "PROPER",
                        "sentiment": {
                            "magnitude": 0.6000000238418579,
                            "score": -0.6000000238418579
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 0.6000000238418579,
                    "score": -0.6000000238418579
                }
            },
            {
                "name": "Storyteller",
                "type": "PERSON",
                "salience": 0.000005848685759701766,
                "mentions": [
                    {
                        "text": {
                            "content": "Storyteller",
                            "beginOffset": -1
                        },
                        "type": "COMMON",
                        "sentiment": {
                            "magnitude": 0.10000000149011612,
                            "score": -0.10000000149011612
                        }
                    }
                ],
                "sentiment": {
                    "magnitude": 11.399999618530273,
                    "score": -0.10000000149011612
                }
            }
        ],
        "documentSentiment": {
            "magnitude": 7.5,
            "score": -0.20000000298023224
        },
        "language": "en"
    }
}
 ```
 
  </p>
</details>

 <details>
  <summary>
     Sample output of a failed text analysis request in case any of the required arguments were not provided
  </summary>
 <p>
 
 ```json
 {
    "status": 0,
    "error": "'text' and 'method' were not passed in the argument"
 }
  ```
  </p>
  
</details> 

 <details>
  <summary>
    Sample output for failed audio analysis response in case an audio file was not provided
  </summary>
 <p>
 
 ```json
  {
    "status": 0,
    "error": "File was not provided or the provided file is not in the following format (WAV, MP3, OGG)"
  }
```
 </p>
 </details>
 

## Running the tests
 ```
python manage.py test
 ```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgment   s

* A lot of functionality was enabled thanks to the Pydub library https://github.com/jiaaro/pydub
* For long audio files, a method created by the following git repo 	https://github.com/akras14/speech-to-text.git was used. 
 However, we made the process of audio encoding and the audio file splitting automatic

