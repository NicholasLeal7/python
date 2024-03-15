#automatização ia teste

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

#inicio - variaveis de descrição
traits = "Mulher Branca, gótica, Cabelo curto escuro (termina no começo do pescoço, não muito volumoso, voltado pra baixo, franja para direita com uma mexa de cabelo branco ), olho verde, rosto fino, velvet Choker, Brinco, Delineado longo. "

personal_traits = "Introspecção: Tendência a ser mais reflexiva e voltada para o mundo interior, com uma apreciação por pensamentos profundos e filosofia. Sensibilidade: Muitas vezes, as mulheres góticas são mais sensíveis às emoções e ao ambiente ao seu redor, podendo ter uma afinidade especial com temas como tristeza, solidão e melancolia.  Individualidade: Valorizam a autenticidade e a expressão pessoal, muitas vezes resistindo às normas sociais convencionais e buscando formas únicas de se expressar. Criatividade: Tendem a ser criativas e artísticas, seja através da música, da escrita, da moda, da arte visual ou de outras formas de expressão criativa. Romantismo: Muitas vezes são românticas no sentido literário da palavra, apreciando o amor idealizado, o mistério e a intensidade emocional. Curiosidade pelo Oculto: Algumas mulheres góticas podem ter uma fascinação pelo ocultismo, pelo sobrenatural e pelo desconhecido, explorando temas como magia, bruxaria e espiritualidade alternativa."

request_prompt = "Crie um promp (em texto) para gerar uma imagem que com uma personagem que possua as características a seguir (todas elas): " + traits + "Agora, para complementar o prompt, idealize de forma aleatória uma atividade ao qual esta personagem poderia estar fazendo, exemplo: ler um livro, ir a praia etc..."

request_desc = "Agora suponha que essa atividade será colocada em uma rede social. Crie uma legenda para o post dessa imagem. Considere a seguinte personalidade da personagem: " + personal_traits
#fim

navegador = webdriver.Chrome()

input()

navegador.get("https://gemini.google.com/app")

time.sleep(2) #aguardar página carregar

navegador.find_element("xpath", "/html/body/div[1]/div[1]/div/div[2]/div[2]/button[1]").click() #clicar em aceitar

time.sleep(2)

navegador.find_element(By.XPATH, "/html/body/chat-app/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/div/div[2]/chat-window/div[1]/div[2]/div[1]/input-area-v2/div/div/div[1]/div/div/rich-textarea").send_keys("oi")
input()






