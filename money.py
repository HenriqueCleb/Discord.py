# Estava pensando em como fazer um sistema de economia para seu bot em python ?????
# Bem , seus problemas acabaram , porque acabou vc acabou de clicar no money.py
# Sabe o que isso significa ????
# Agora vc poderá criar o seu tão sonhado sistema de dinheiros no discord
# Chega de comentarios super desconexos e inuteis ( pq de inutil aqui já basta vc)


import discord 
import datetime
import sqlite3
from discord.ext import commands, tasks
from datetime import date
# Usei sqlite3 pq é um metoodo mais facil e bla bla bla 
# Importação dos modulos e das funções dos mesmos
# Isso aqui tu já sabe nem tem pq eu estar falando

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.guilds = True
# Programaticamente isso aqui tá errado no discord.py , mas ta funcionando no meu bot , entt é isso 
# Os intents servem pra auxiliar o bot na hora de indentificar as funções como por exemplo nas reactions

client = commands.Bot(command_prefix='*', help_command= None)
# Isso aqui é obrigatorio , aqui vc define o prefixo do seu bot e se vai ter ou não a função do comando help , se vc quiser fazer um comando help personalizado eu aconselho vc a deixar o help_command em None


#conectores
connect = sqlite3.connect("clients.db")
# Aqui vc cria uma conexão com o banco de dados que vai se chamar "clients.db"
cursor = conect.cursor()
# Essa função vai criar um cursor pra sua tabela 
cursor.execute("CREATE TABLE transações (id integer, transações text)")
# Essa parte é importante lembra que o seu codigo deve ser executado duas vezes , sendo a primeira para a criação do banco de dados , e dps que já tiver sido executado 
# o vc deve colocar o cursor.execute acima na forma de comentario

@client.command()
@commands.cooldown(1,86400,commands.BucketType.user)
# Com isso aqui vc vai dizer ao seu bot que cada usuario só vai poder pegar o daily uma vez a cada 24 horas 
async def daily(ctx):
  name = f'{ctx.author.name}#{ctx.author.discriminator}'
  nome = f'{ctx.author.id}#{ctx.author.discriminator}'
  valor =  random.randint(100,3000)
  valor_i = 0
  try :
      with conect :
          cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(ctx.author.id, valor_i, 'solteiro(a)', name ))
          cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(ctx.author.id, valor_i, 'solteiro(a)', nome))
          cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
          dinheiro = cursor.fetchone()
          sla= dinheiro[0]
          valor_final = sla + valor
          cursor.execute("UPDATE clients SET money = '"+str(valor_final)+"' WHERE id = '"+str(ctx.author.id)+"' ")
          conect.commit()
          
          
          hora_daily1 = datetime.datetime.now()
          texto =f '''
          Você só poderá pegar seu daily amanhã as {hora_daily1.hour}:{hora_daily1.minute}
          '''
          # Basicamente aqui em cima vai ser verificado se o usuario já está no banco de dados , caso ele não estiver , ele será adicioando com a nova quantia de money
          await ctx.reply(f'|Parabens {ctx.author.mention} você ganhou {valor}ki-coins!!|\nAgora vc tem {valor_final}ki-coins')
          
    except sqlite3.IntegrityError :
      cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
      dinheiro = cursor.fetchone()
      bom = dinheiro[0]
      valor_final = bom + valor
      cursor.execute("UPDATE clients SET money = '"+str(valor_final)+"' WHERE id = '"+str(ctx.author.id)+"' ")
      conect.commit()
      hora_exata = datetime.datetime.now()
      text = f'''
      Você só poderá pegar seu daily novamente amanhã as {hora_exata.hour}:{hora_exata.minute}
      '''
      await ctx.reply(f'|Parabens {ctx.author.mention} vc ganhou {valor} ki-coins!!|\nAgora vc tem {valor_final}ki-coins')
      
      
     
      
      
      
