# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import requests

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
#from ask_sdk_model import Request, Response
from ask_sdk_model import Response
from ask_sdk_model.interfaces.audioplayer import (
    PlayDirective, PlayBehavior, AudioItem, Stream, AudioItemMetadata,
    StopDirective, ClearQueueDirective, ClearBehavior)


from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

URL = "https://0a9c-2001-16b8-2d8c-5900-1507-3185-ea6e-9d39.ngrok.io/" 

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hallo, ich bin Alexa deine Freundin. Hast du Lust mit mir zu spielen? Wenn ja, schrei spielen!!!."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class spielenIntentHandler(AbstractRequestHandler):
    """Handler for spielen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("spielen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/huhn2.mp3"/>' + "Na, wen haben wir den da gerade geh??rt? Nenne mir das passende Tier."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HuhnIntentHandler(AbstractRequestHandler):
    """Handler for Huhn Intent."""
    def can_handle(self, handler_input):
        
        return ask_utils.is_intent_name("huehner")(handler_input)
    
    def handle(self, handler_input):
        
        speak_output = '<amazon:domain.name = "fun"> "Ja genau das sind unsere H??hner und unser Hahn G??nther. Wenn du mir die richtige Zahl nennen kannst wie viele H??hner auf deiner Karte sind, kann ich dir was ??ber H??hner erz??hlen" </amazon:domain>'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
          )  

class huhnbildIntentHandler(AbstractRequestHandler):
    """Handler for huhnbild Intent."""
    def can_handle(self, handler_input):
        
        return ask_utils.is_intent_name("huhnbild")(handler_input)
    
    def handle(self, handler_input):
        
        speak_output = "Typisch f??r H??hner sind der rote Kamm und die Kehllappen am Kopf. Vor allem bei den H??hnen ist der Kamm sehr gro??. sie sind V??gel, die die meiste Zeit auf dem Boden leben. Sie k??nnen zwar nicht besonders gut fliegen, aber daf??r k??nnen sie mit ihren kr??ftigen Beinen umso schneller rennen. H??hner k??nnen ziemlich schlecht in die ferne sehen. Sie haben nur vier Zehen und keine Federn an den Beinen. Lass uns weitergehen die anderen Tiere auf Bauer Hermanns Hof besuchen. Falls du mein R??tsel l??sen kannst, k??nnen wir weiter zu meinen Lieblingstieren gehen. Mein Lieblingstier ist gro??, hatt Flecken und macht Muh. Was ist mein Lieblingstier?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
          )  

class KuhIntentHandler(AbstractRequestHandler):
    """Handler for Kuh Intent."""
    def can_handle(self, handler_input):
        
        return ask_utils.is_intent_name("Kuh")(handler_input)
    
    def handle(self, handler_input):
        
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Kuh+2.mp3"/>' + "Ah und da ist ja auch schon Bauer Herrmann er melkt die K??he. Lass uns schnell Bauer Herrmann helfen dann kann er uns den Rest von seinem Hof zeigen. Lass uns Bauer Hermann begr????en?" 
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )  

class HerrHermannIntentHandler(AbstractRequestHandler):
    """Handler for HerrHerrmann Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HerrHermann")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output =  '<voice name="Hans"> "Hallo, wie geht es dir? Sch??n das du mich auf meinem Bauernhof besuchen kommst. Wenn willst du den besuchen? Unsere Pferde Schatten fell und Rudolf oder willst du mit mir die Katzen auf meinem Hof suchen?" </voice>'
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
                
        )        

#audio pferdelauf
#audio pferdewiehern
class pferdIntentHandler(AbstractRequestHandler):
    """Handler for pferd Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pferd")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Pferdlaufen2.mp3"/>' +'<voice name="Hans"> Da sind wir ja schon bei meinen Pferden. Immer wenn ich in die N??he von ihrer Koppel komme, kommen Schatten fell und Rudolf angallopiert, als Belohnung bekommmen sie immer ihre t??gliche Karotte. Wenn du noch mehr ??ber Pferde wissen willst zeige mir bitte die Karte mit dem Pferd drauf</voice>' 
        data = requests.get(URL+'animal').json()[0]

        return (
            handler_input.response_builder
                .speak(speak_output + data)
                .ask(speak_output)
                .response
        )

class pferdebildIntentHandler(AbstractRequestHandler):
    """Handler for pferdebild Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pferdebild")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Pferde geh??ren zu den so genannten Einhufern: Dieser Name beschreibt was sie von allen anderen Huftieren unterscheidet: Der Mittelzeh ihres Hufes ist in Form eines einzigen Hufs entwickelt Der Kopf der Pferde ist gro?? und l??nglich. Die Augen sitzen an den Seiten des Kopfes Typisch sind au??erdem die M??hne und der Schweif. Die vier langen Beine machen die Pferde zu schnellen L??ufern. Jetzt wei??t du ja schon viel ??ber Pferde lass uns meine Katzen suchen. Sag bescheid wenn du bereit bist" </voice>'
#wen falsches bild: Von hier aus kann ich zwei Wege gehen. Der eine Weg f??hrt und zu den Schweinen und der andere f??hrt uns zu dem Hof wo wir meine Katzen suchen k??nnen.M??chtest zu du lieber zu den Katzen oder zu den Schweinen?

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class katzeIntentHandler(AbstractRequestHandler):
    """Handler for katze Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("katze")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Ok dann lass uns zu dem Hof gehen und meine Katzen kennenlernen. Meine drei Katzen hei??en figaro, simba und mufasa. Magst du lieber drinnen nach den Katzen suchen suchen oder drau??en ?"</voice>'
        #audiokatze = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Hund+und+Schaf2.mp3"/>'
        #AudioKatzen Da ist nacho sie hat Hunger. Vielleicht hat sie heute keine Maus gefunden? Ich muss sie schnell f??ttern dann k??nnen wir die anderen Katzen suchen. Wo k??nnten sich meine Katzen simba, figaro und mufasa verstecken? Ich glaube ich habe da schon so eine Idee figaro liebt es sich in meinen Bett gem??tlich zu machen vielleicht finden wir ihn da. simba und mufasa lieben es drau??en zu sein vielleicht finden wir sie drau??en. Wo willst du zuerst suchen drinnen oder drau??en?" </voice>'

        return (
            handler_input.response_builder
                .speak(speak_output+audiokatze)
                .ask(speak_output)
                .response
        )
class drinnenIntentHandler(AbstractRequestHandler):
    """Handler for drinnen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("drinnen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Ok lass uns mal ins Schlafzimmer gehen ich bin mir sicher das figaro der kleine Faul??nzer sich dort versteckt. Nat??rlich ist figaro hier. Toll du hast figaro gefunden. Hier drinnen haben wir nichts mehr zu entdecken, lass und raus gehen, um raus zu gehen sag einfach raus" </voice>'

        return (
            handler_input.response_builder
                .speak(speak_output )
                .ask(speak_output)
                .response
        )
class rausIntentHandler(AbstractRequestHandler):
    """Handler for raus Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("raus")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Klar bei so einem sch??nen Wetter sollte man die Sonne drau??en genie??en. Lass uns in meinem Garten kurz ausruhen. Schau mal auf deine Karten,hier gibt es eine Karte auf der du meinen Garten siehst. Wenn genau schaust siehst du auch zwei Katzen auf dem Bild. Kannst du mir sagen wo sie sind?" </voice>'

        return (
            handler_input.response_builder
                .speak(speak_output )
                .ask(speak_output)
                .response
        )
class blumeIntentHandler(AbstractRequestHandler):
    """Handler for blume Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("blume")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Ja genau simba ist bei den Blumen.In meinem Garten ist noch ein Tier kannst du mir die passende Karte mit dem Bild drauf zeigen?" </voice>'    
        data = requests.get(URL+'animal').json()[0]
        
        return (
            handler_input.response_builder
                .speak(speak_output + data)
                .ask(speak_output)
                .response
        )
class bulldogIntentHandler(AbstractRequestHandler):
    """Handler for bulldog Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("bulldog")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Ja super beim Traktor ist mufasa. Aber mufasa ist nicht alleine bello ist auch da. Kannst du mir zeigen welches Tier bello ist, du findest in deinen Karten das passende Bild ?" </voice>'
        data = requests.get(URL+'animal').json()[0]
        
        return (
            handler_input.response_builder
                .speak(speak_output + data)
                .ask(speak_output)
                .response
        )
        
        #AudioTracktor
        #INTENT HUND "ja genau im garten ist auch bello mein Hund. Er wartet auf mich ,weil er wei?? das wir noch zu den Schafen fahren m??ssen um sie wieder zur??ck in ihren Stall zu bringen. Auf zu den schafen zeig mir das bild mit dem Schaf und der Traktor kann starten " 
class hundbildIntentHandler(AbstractRequestHandler):
    """Handler for hundbild Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("hundbild")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Hund2.mp3"/>' + '<voice name="Hans"> "Genau Bello ist ein Hund richtig. Sobald du LOS sagst kannst, kann der Traktor starten." </voice>'
        return (
            handler_input.response_builder
                .speak(speak_output )
                .ask(speak_output)
                .response
        )

class schafeundbelloIntentHandler(AbstractRequestHandler):
    """Handler for schafeundbello Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("schafeundbello")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Ja genau Bello h??tet meine Schafe. Ich kann sogar schon die schafe h??ren. Wir sind  fast da. Wenn du Auf gehts sagst, dann holt bello die Schafe zu uns." </voice>'
        
        return (
            handler_input.response_builder
                .speak(speak_output )
                .ask(speak_output)
                .response
        )
class aufgehtsIntentHandler(AbstractRequestHandler):
    """Handler for aufgehts Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aufgehts")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Hund+und+Schaf2.mp3"/>' + '<voice name="Hans"> "Schau das sind meine schafe, sind die nicht weich. Aus Ihrer Wolle kann man M??tzen, Pullover und weitere Sachen machen und auch Milch bekomme ich jeden Tag von meinen Schafen. Damit kann ich dann K??se herstellen. Wenn du mehr ??ber Schafe wissen willst zeige mir die passende Karte." </voice>'
        data = requests.get(URL+'animal').json()[0]
        
        return (
            handler_input.response_builder
                .speak(speak_output + data)
                .ask(speak_output)
                .response
        )
# aufgehtsintent " audio Schau das sind meine schafe. sind die nicht weich. Aus Ihrer Wolle kann man M??tzen , Pulover und weitere Sachen machen und auch Milch bekomme ich jeden Tag von meinen Schafen. Damit kann ich dann K??se herstellen. Wenn du mehr ??ber Schafe wissen willst zeige mir die passende Karte. "
# schaf intent " ja schafe h??tet bello.chau das sind meine schafe. sind die nicht weich. Aus Ihrer Wolle kann man M??tzen , Pulover und weitere Sachen machen und auch Milch bekomme ich jeden Tag von meinen Schafen. Damit kann ich dann K??se herstellen. Wenn du mehr ??ber Schafe wissen willst zeige mir die passende Karte."
class schafIntentHandler(AbstractRequestHandler):
    """Handler for schaf Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("schaf")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Schafe ??? und vor allem die jungen L??mmchen ??? sind sehr friedliche Tiere. Die M??nnchen hei??en Widder und sind sehr viel gr????er und st??rker als die weiblichen Schafe. Die jungen Schafe im Alter bis zu einem Jahr werden L??mmer genannt. Viele Schafe tragen H??rner: Bei den Wildschafen sind sie entweder schneckenf??rmig gekr??mmt, lang und spiralig gewunden oder kurz und nur leicht gebogen. Die H??rner der Weibchen sind kleiner und manche Hausschafe tragen, je nach Rasse, oft gar keine H??rner.Ein typisches Kennzeichen der Schafe ist ihr Fell, das zu Wolle verarbeitet wird. Es kann wei??, grau, braun, schwarz oder auch gemustert sein und besteht aus der dichten, gekr??uselten Unterwolle und den dar??ber liegenden dickeren Haaren. Schau mal da kommt auch schon wieder Alexa deine Freundin. Ich hoffe dir hatt mein Hof gefallen wenn du Lust hast schau einfach wieder vorbei bei uns ist immer was los. Bis zum n??chsten mal." </voice>'
        
        return (
            handler_input.response_builder
                .speak(speak_output )
                .ask(speak_output)
                .response
        )

class losIntentHandler(AbstractRequestHandler):
    """Handler for los Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("losIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Traktor2.mp3"/>' + '<voice name="Hans">"F??r viele ist er der beste Freund: Hunde leben seit Jahrtausenden bei den Menschen. Hunde sind nicht nur treue Gef??hrten, sondern auch Wach-, H??te- und Suchhunde. Der Haushund stammt vom Wolf ab: Bei manchen Rassen wie etwa dem Deutschen Sch??ferhund ist das auch noch deutlich zu sehen. Ansonsten aber sehen sie sehr verschieden aus: Von den vielen verschiedenen Hunderassen gleicht keine der anderen. Alle  Hunden haben  gemeinsam , dass sie einen Schwanz besitzen sowie sehr gut h??ren und hervorragend riechen k??nnen. Au??erdem k??nnen sie prima laufen und schwimmen. Ich habe ein kleines R??tsel f??r dich. Bello ist ein Sch??ferhund was h??tet er?" </voice>'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class bereitIntentHandler(AbstractRequestHandler):
    """Handler for bereit Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("bereitIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Ok lass uns die Katzen Suchen. Meine drei Katzen hei??en figaro, simba und mufasa. Magst du lieber drinnen nach den Katzen suchen suchen oder drau??en?" </voice>'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "hilfe"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Erst die Rechte, dann die Linke beide machen winke, winke!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(spielenIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HuhnIntentHandler())
sb.add_request_handler(huhnbildIntentHandler())
sb.add_request_handler(KuhIntentHandler())
sb.add_request_handler(HerrHermannIntentHandler())
sb.add_request_handler(pferdIntentHandler())
sb.add_request_handler(pferdebildIntentHandler())
sb.add_request_handler(katzeIntentHandler())
sb.add_request_handler(drinnenIntentHandler())
sb.add_request_handler(rausIntentHandler())
sb.add_request_handler(blumeIntentHandler())
sb.add_request_handler(bulldogIntentHandler())
sb.add_request_handler(losIntentHandler())
sb.add_request_handler(bereitIntentHandler())
sb.add_request_handler(hundbildIntentHandler()) 
sb.add_request_handler(schafeundbelloIntentHandler())
sb.add_request_handler(aufgehtsIntentHandler())
sb.add_request_handler(schafIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()