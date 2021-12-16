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

URL = "https://7c0a-2001-4ca0-0-f238-888a-527c-72a3-2376.ngrok.io/" 

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = 'Hallo, ich bin Alexa deine Freundin. Hast du Lust mit mir zu spielen? Wenn ja, schrei spielen!!!.'  
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
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/huhn2.mp3"/>' + "Na, wen haben wir den da gerade gehört? Nenne mir das passende Tier."

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
        
        speak_output = "Ja genau das sind unsere Hühner und unser Hahn Günther. Wenn du mir die richtige Zahl nennen kannst wie viele Hühner auf deiner Karte sind, kann ich dir was über Hühner erzählen"

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
        
        speak_output = "Typisch für Hühner sind der rote Kamm und die Kehllappen am Kopf. Vor allem bei den Hähnen ist der Kamm sehr groß. sie sind Vögel, die die meiste Zeit auf dem Boden leben. Sie können zwar nicht besonders gut fliegen, aber dafür können sie mit ihren kräftigen Beinen umso schneller rennen. Hühner können ziemlich schlecht in die ferne sehen. Sie haben nur vier Zehen und keine Federn an den Beinen. Lass uns weitergehen die anderen Tiere auf Bauer Hermanns Hof besuchen. Falls du mein Rätsel lösen kannst, können wir weiter zu meinen Lieblingstieren gehen. Mein Lieblingstier ist groß, hatt Flecken und macht Muh. Was ist mein Lieblingstier?"

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
        
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Kuh+2.mp3"/>' + "Ah und da ist ja auch schon Bauer Herrmann er melkt die Kühe. Lass uns schnell Bauer Herrmann helfen dann kann er uns den Rest von seinem Hof zeigen. Lass uns Bauer Hermann begrüßen?" 
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
        speak_output =  '<voice name="Hans"> "Hallo, wie geht es dir? Schön das du mich auf meinem Bauernhof besuchen kommst. Wenn willst du den besuchen? Unsere Pferde Schatten fell und Rudolf oder willst du mit mir die Katzen auf meinem Hof suchen?" </voice>'
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
                
        )        

#schweine audio 
#class schweinIntentHandler(AbstractRequestHandler):
 #   """Handler for schwein Intent."""
  #  def can_handle(self, handler_input):
   #     # type: (HandlerInput) -> bool
    #    return ask_utils.is_intent_name("schwein")(handler_input)
#
 #   def handle(self, handler_input):
        # type: (HandlerInput) -> Response
  #      speak_output = "Hier sind wir bei unseren Schweinen Leon, Piggy und Sigmunde. #AudioSchwein. Schweine sind wirklich interessante Tiere. Was machen den schweine am liebsten zeige mir das passende Bild?" 

   #     return (
    #        handler_input.response_builder
     #           .speak(speak_output)
      #          .ask(speak_output)
       #         .response
        #)
#class essenschweineIntentHandler(AbstractRequestHandler):
 #   """Handler for essenschweine Intent."""
  #  def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
   #     return ask_utils.is_intent_name("essenschweine")(handler_input)

    #def handle(self, handler_input):
        # type: (HandlerInput) -> Response
     #   speak_output = "Meine Schweine essen wirklich gerne. Wusstest du, das Schweine es lieben mit dem Rüssel im Boden nach Nahrung zu wühlen. Unter naturnahen Bedingungen beschäftigen sie sich zu 70 % bis 80 % mit der Nahrungssuche. willst du noch mehr über Schweine erfahren, dann zeige mir das Bild mit dem Schwein drauf." 

      #  return (
       #     handler_input.response_builder
        #        .speak(speak_output)
         #       .ask(speak_output)
          #      .response
        #)
#class schweinebildIntentHandler(AbstractRequestHandler):
 #   """Handler for schweinebild Intent."""
  #  def can_handle(self, handler_input):
   #     # type: (HandlerInput) -> bool
    #    return ask_utils.is_intent_name("schweinebild")(handler_input)

    #def handle(self, handler_input):
        # type: (HandlerInput) -> Response
     #   speak_output = "Schweine haben einen großen Kopf, einen kurzen Hals und kurze Beine. Typisch sind die kegelförmige Form des Kopfes und die lange bewegliche Schnauze mit den Nasenöffnungen in der Rüsselscheibe. Die Augen sind klein und sitzen hoch am Kopf, die Ohren laufen spitz zu und hängen oft nach vorn. Der Schwanz trägt manchmal eine Quaste. Sie können sehr gut riechen und hören, sehen aber schlecht. Viele Schweine haben kein Fell, sondern tragen nur ein mehr oder weniger dichtes Borstenkleid, durch das die rosa Haut hindurch schimmert. Es gibt aber auch Schweine , die dunkel gefärbt sind oder ein dunkles Muster tragen - das Bentheimer Hausschwein zum Beispiel hat große dunkle Flecken auf hellem Grund. lass uns zurück zum hof gehen, magst du auf unserem rückweg zum Hof bei den Pferden vorbeischauen oder direkt zum hof?" 

      #  return (
       #     handler_input.response_builder
        #        .speak(speak_output)
         #       .ask(speak_output)
          #      .response
        #)
#class schweineschlamIntentHandler(AbstractRequestHandler):
 #   """Handler for schweineschlam Intent."""
  #  def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
   #     return ask_utils.is_intent_name("schweineschlam")(handler_input)

   # def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output = "Ja genau. Das machen unsere drei schweine am liebsten besonders gerne machen sie es aber wenn es warm ist. Dann nutzen sie es zur Abkühlung.Magst du noch mehr über Schweine wissen oder dich auf den Rückweg zum Hof machen? Zeige mir das passende Bild" 

        #return (
         #   handler_input.response_builder
          #      .speak(speak_output)
           #     .ask(speak_output)
            #    .response
        #)
#audio pferdelauf
#audio pferdewiehern
class pferdIntentHandler(AbstractRequestHandler):
    """Handler for pferd Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pferd")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Pferdlaufen2.mp3"/>' +'<voice name="Hans"> Da sind wir ja schon bei meinen Pferden. Immer wenn ich in die Nähe von ihrer Koppel komme, kommen Schatten fell und Rudolf angallopiert, als Belohnung bekommmen sie immer ihre tägliche Karotte. Wenn du noch mehr über Pferde wissen willst zeige mir bitte die Karte mit dem Pferd drauf</voice>' 
        data = requests.get(URL+'animal').json()[0]

        return (
            handler_input.response_builder
                .speak(speak_output + data)
                .ask(speak_output)
                .response
        )
#class halloIntentHandler(AbstractRequestHandler):
    #"""Handler for hallo Intent."""
    #def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        #return ask_utils.is_intent_name("hallo")(handler_input)

    #def handle(self, handler_input):
        # type: (HandlerInput) -> Response
       # speak_output = "Das Pferd hat die größten Augen aller am Land lebenden Säugetiere. Wenn du noch mehr über Pferde wissen willst zeige mir das passende Bild." 

        #return (
          #  handler_input.response_builder
            #    .speak(speak_output)
            #    .ask(speak_output)
             #   .response
        #)

class pferdebildIntentHandler(AbstractRequestHandler):
    """Handler for pferdebild Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pferdebild")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Pferde gehören zu den so genannten Einhufern: Dieser Name beschreibt was sie von allen anderen Huftieren unterscheidet: Der Mittelzeh ihres Hufes ist in Form eines einzigen Hufs entwickelt Der Kopf der Pferde ist groß und länglich. Die Augen sitzen an den Seiten des Kopfes Typisch sind außerdem die Mähne und der Schweif. Die vier langen Beine machen die Pferde zu schnellen Läufern. Jetzt weißt du ja schon viel über Pferde lass uns meine Katzen suchen. Sag bescheid wenn du bereit bist" </voice>'
#wen falsches bild: Von hier aus kann ich zwei Wege gehen. Der eine Weg führt und zu den Schweinen und der andere führt uns zu dem Hof wo wir meine Katzen suchen können.Möchtest zu du lieber zu den Katzen oder zu den Schweinen?

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
        speak_output = '<voice name="Hans"> "Ok dann lass uns zu dem Hof gehen und meine Katzen kennenlernen. Meine drei Katzen heißen figaro, simba und mufasa. Magst du lieber drinnen nach den Katzen suchen suchen oder draußen ?"</voice>'
        #audiokatze = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Hund+und+Schaf2.mp3"/>'
        #AudioKatzen Da ist nacho sie hat Hunger. Vielleicht hat sie heute keine Maus gefunden? Ich muss sie schnell füttern dann können wir die anderen Katzen suchen. Wo könnten sich meine Katzen simba, figaro und mufasa verstecken? Ich glaube ich habe da schon so eine Idee figaro liebt es sich in meinen Bett gemütlich zu machen vielleicht finden wir ihn da. simba und mufasa lieben es draußen zu sein vielleicht finden wir sie draußen. Wo willst du zuerst suchen drinnen oder draußen?" </voice>'

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
        speak_output = '<voice name="Hans"> "Ok lass uns mal ins Schlafzimmer gehen ich bin mir sicher das figaro der kleine Faulänzer sich dort versteckt. Natürlich ist figaro hier. Toll du hast figaro gefunden. Hier drinnen haben wir nichts mehr zu entdecken, lass und raus gehen, um raus zu gehen sag einfach raus" </voice>'

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
        speak_output = '<voice name="Hans"> "Klar bei so einem schönen Wetter sollte man die Sonne draußen genießen. Lass uns in meinem Garten kurz ausruhen. Schau mal auf deine Karten,hier gibt es eine Karte auf der du meinen Garten siehst. Wenn genau schaust siehst du auch zwei Katzen auf dem Bild. Kannst du mir sagen wo sie sind?" </voice>'

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


    

        #Katze audio1 
#class katzeeinsheubodenIntentHandler(AbstractRequestHandler):
 #   """Handler for katzeinsheuboden Intent."""
  #  def can_handle(self, handler_input):
   #     # type: (HandlerInput) -> bool
    #    return ask_utils.is_intent_name("katzeeinsheuboden")(handler_input)
#
 #   def handle(self, handler_input):
  #      # type: (HandlerInput) -> Response
   #     speak_output = "Der Heuboden befindet sich meist über dem Stall. hier lager ich getrocknetes Grass was ich im Sommer von meinen Feldern einsammel und an meine Kühe und Pferde im Winter verfüttere. Hier ist ja auch Simba #Audio Katze 1. Ich glaube Bounty möchte alleine sein. Lass uns gehen. Zeig mir dein Bild wenn du noch mehr über Katzen erfahren willst." 
     #   return (
    #        handler_input.response_builder
      #          .speak(speak_output)
       #         .ask(speak_output)
        #        .response
        #)
        #Garten Bild
#class katzezweigartenIntentHandler(AbstractRequestHandler):
 #   """Handler for katzezweigarten Intent."""
  #  def can_handle(self, handler_input):
   #     # type: (HandlerInput) -> bool
 #       return ask_utils.is_intent_name("katzezweigarten")(handler_input)
#
  #  def handle(self, handler_input):
   #     # type: (HandlerInput) -> Response
    #    speak_output = "Im Garten sind Figaro und mufasa sie spielen mit Ihrem Spielzeug. Zeig mir dein Bild wenn du noch mehr über Katzen erfahren willst." 
     #   return (
      #      handler_input.response_builder
       #         .speak(speak_output)
        #        .ask(speak_output)
         #       .response
        #)
        #Tracktor Bild

        #Stall Bild
#class KatzeStallIntentHandler(AbstractRequestHandler):
 #   """Handler for KatzeStall Intent."""
  #  def can_handle(self, handler_input):
   #     # type: (HandlerInput) -> bool
    #    return ask_utils.is_intent_name("KatzeStall")(handler_input)

    #def handle(self, handler_input):
        # type: (HandlerInput) -> Response
     #   speak_output = "'Im Stall ist keine meiner Katzen, aber wenn du willst können wir im Stall die Schweine besuchen. Möchtest du noch die weiteren Katzen suchen oder bei den Schweinen bleiben?" 
      #  return (
       #     handler_input.response_builder
        #        .speak(speak_output)
         #       .ask(speak_output)
          #      .response
        #)
        #audio bello
        #katzebildfalsch
#class katzebildIntentHandler(AbstractRequestHandler):
 #   """Handler for katzebild Intent."""
  #  def can_handle(self, handler_input):
   #     # type: (HandlerInput) -> bool
    #    return ask_utils.is_intent_name("katzebild")(handler_input)

    #def handle(self, handler_input):
        # type: (HandlerInput) -> Response
     #   speak_output = "Katzen sind sehr beliebte, aber auch eigenwillige Haustiere: Manchmal sind sie kratzbürstig dann wieder verschmust und verspielt.Am Verhalten von Katzen könnt ihr ganz leicht ihre Stimmung ablesen. Manchmal wollen sie ihre Ruhe haben und dann brauchen sie wieder viel Aufmerksamkeit.In der Familie der Katzen gibt es zwei große Gruppen: Die Kleinkatzen, zu denen unsere Hauskatzen und zum Beispiel auch die Gepaden gehören, und Großkatzen wie Löwen und Tiger. Katzen können ihre Krallen einziehen. Wenn sie angreifen, können sie sie blitzschnell vorschnellen lassen Katzen können sich sehr geschickt bewegen und klettern und sehr gut hören und sehen - auch in der Dunkelheit. Da begrüßt uns ja auch schon Bello. #Audio Hund. Wenn du magst kann ich dir was über Hunde auf der Fahrt erzählen, wenn du mir das Bild von Bello dem Hund zeigen kannst." 
      #  return (
       #     handler_input.response_builder
        #        .speak(speak_output) 
         #       .ask(speak_output)
          #      .response
         #)
        
        #AudioTracktor
        #INTENT HUND "ja genau im garten ist auch bello mein Hund. Er wartet auf mich ,weil er weiß das wir noch zu den Schafen fahren müssen um sie wieder zurück in ihren Stall zu bringen. Auf zu den schafen zeig mir das bild mit dem Schaf und der Traktor kann starten " 
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
#class hasebildIntentHandler(AbstractRequestHandler):
    #"""Handler for hasebild Intent."""
    #def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        #return ask_utils.is_intent_name("hasebild")(handler_input)

    #def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output = "Ja genau. So sieht der Feldhase aus. Möchtest du noch was über Feldhasen lernen?, dan sag hoppelhase" 
        
        #return (
            #handler_input.response_builder
                #.speak(speak_output )
                #.ask(speak_output)
                #.response
        #)
        #helender übergang zu schaffen
#class hoppelhaseIntentHandler(AbstractRequestHandler):
    #"""Handler for hoppelhase Intent."""
    #def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        #return ask_utils.is_intent_name("hoppelhase")(handler_input)

    #def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output = "Feldhasen sind scheu, schnell und dank ihrer langen Ohren wirklich unverkennbar. Außerdem haben sie als Osterhase Karriere gemacht.Wie die Kaninchen sind auch Feldhasen nicht mit den Nagetieren verwandt.Die langen Ohren sind die Markenzeichen des Feldhasen Typisch sind auch die kräftigen Hinterbeine und die langen HinterfüßeFeldhasen haben ein langes Fell aus Wollhaaren und Deckhaaren. Es ist gelblich grau bis ockerbraun oder braunrot und manchmal schwarz gesprenkelt. Das Fell der Beine ist hellbraun. Die Ohren sind grau und haben an der Spitze einen schwarzen, dreieckigen Fleck. Der Schwanz, er wird auch Blume genannt, ist oben schwarz und unten weiß.Die Fellfarbe kann sich aber mit der Jahreszeit leicht verändern: Im Winter werden die Tiere am Kopf meist weißer und an den Hüften eher grau." 
        
        #return (
            #handler_input.response_builder
                #.speak(speak_output )
                #.ask(speak_output)
                #.response
        #)
        #audiotracktor
        #audiobello
        #audioschafe
class schafeundbelloIntentHandler(AbstractRequestHandler):
    """Handler for schafeundbello Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("schafeundbello")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Ja genau Bello hütet meine Schafe. Ich kann sogar schon die schafe hören. Wir sind  fast da. Wenn du Auf gehts sagst, dann holt bello die Schafe zu uns." </voice>'
        
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
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Hund+und+Schaf2.mp3"/>' + '<voice name="Hans"> "Schau das sind meine schafe, sind die nicht weich. Aus Ihrer Wolle kann man Mützen, Pullover und weitere Sachen machen und auch Milch bekomme ich jeden Tag von meinen Schafen. Damit kann ich dann Käse herstellen. Wenn du mehr über Schafe wissen willst zeige mir die passende Karte." </voice>'
        data = requests.get(URL+'animal').json()[0]
        
        return (
            handler_input.response_builder
                .speak(speak_output + data)
                .ask(speak_output)
                .response
        )
# aufgehtsintent " audio Schau das sind meine schafe. sind die nicht weich. Aus Ihrer Wolle kann man Mützen , Pulover und weitere Sachen machen und auch Milch bekomme ich jeden Tag von meinen Schafen. Damit kann ich dann Käse herstellen. Wenn du mehr über Schafe wissen willst zeige mir die passende Karte. "
# schaf intent " ja schafe hütet bello.chau das sind meine schafe. sind die nicht weich. Aus Ihrer Wolle kann man Mützen , Pulover und weitere Sachen machen und auch Milch bekomme ich jeden Tag von meinen Schafen. Damit kann ich dann Käse herstellen. Wenn du mehr über Schafe wissen willst zeige mir die passende Karte."
class schafIntentHandler(AbstractRequestHandler):
    """Handler for schaf Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("schaf")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<voice name="Hans"> "Schafe – und vor allem die jungen Lämmchen – sind sehr friedliche Tiere. Die Männchen heißen Widder und sind sehr viel größer und stärker als die weiblichen Schafe. Die jungen Schafe im Alter bis zu einem Jahr werden Lämmer genannt. Viele Schafe tragen Hörner: Bei den Wildschafen sind sie entweder schneckenförmig gekrümmt, lang und spiralig gewunden oder kurz und nur leicht gebogen. Die Hörner der Weibchen sind kleiner und manche Hausschafe tragen, je nach Rasse, oft gar keine Hörner.Ein typisches Kennzeichen der Schafe ist ihr Fell, das zu Wolle verarbeitet wird. Es kann weiß, grau, braun, schwarz oder auch gemustert sein und besteht aus der dichten, gekräuselten Unterwolle und den darüber liegenden dickeren Haaren. Schau mal da kommt auch schon wieder Alexa deine Freundin. Ich hoffe dir hatt mein Hof gefallen wenn du Lust hast schau einfach wieder vorbei bei uns ist immer was los. Bis zum nächsten mal." </voice>'
        
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
        speak_output = '<audio src="https://audiokidsskillfarm.s3.eu-west-1.amazonaws.com/Traktor2.mp3"/>' + '<voice name="Hans">"Für viele ist er der beste Freund: Hunde leben seit Jahrtausenden bei den Menschen. Hunde sind nicht nur treue Gefährten, sondern auch Wach-, Hüte- und Suchhunde. Der Haushund stammt vom Wolf ab: Bei manchen Rassen wie etwa dem Deutschen Schäferhund ist das auch noch deutlich zu sehen. Ansonsten aber sehen sie sehr verschieden aus: Von den vielen verschiedenen Hunderassen gleicht keine der anderen. Alle  Hunden haben  gemeinsam , dass sie einen Schwanz besitzen sowie sehr gut hören und hervorragend riechen können. Außerdem können sie prima laufen und schwimmen. Ich habe ein kleines Rätsel für dich. Bello ist ein Schäferhund was hütet er?" </voice>'

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
        speak_output = '<voice name="Hans"> "Ok lass uns die Katzen Suchen. Meine drei Katzen heißen figaro, simba und mufasa. Magst du lieber drinnen nach den Katzen suchen suchen oder draußen?" </voice>'

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
#sb.add_request_handler(schweinIntentHandler())
#sb.add_request_handler(essenschweineIntentHandler())
#sb.add_request_handler(schweinebildIntentHandler())
#sb.add_request_handler(schweineschlamIntentHandler())
sb.add_request_handler(pferdIntentHandler())
#sb.add_request_handler(halloIntentHandler())
sb.add_request_handler(pferdebildIntentHandler())
sb.add_request_handler(katzeIntentHandler())
sb.add_request_handler(drinnenIntentHandler())
sb.add_request_handler(rausIntentHandler())
sb.add_request_handler(blumeIntentHandler())
sb.add_request_handler(bulldogIntentHandler())
sb.add_request_handler(losIntentHandler())
sb.add_request_handler(bereitIntentHandler())
#sb.add_request_handler(katzeeinsheubodenIntentHandler())
#sb.add_request_handler(katzezweigartenIntentHandler())
#sb.add_request_handler(KatzeStallIntentHandler())
#sb.add_request_handler(katzebildIntentHandler())
sb.add_request_handler(hundbildIntentHandler()) 
#sb.add_request_handler(hasebildIntentHandler())
#sb.add_request_handler(hoppelhaseIntentHandler())   
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