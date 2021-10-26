from operator import ifloordiv
from discord import guild
from discord.message import DeletedReferencedMessage
import sqlite3
import discord
from discord.ext import commands,tasks
from itertools import cycle
import os
import time
import asyncio
import datetime
from datetime import date
import random
from discord import Embed
from discord import Guild
#os.chdir('C:\Users\Pc\AppData\Local\Temp\Rar$DIa7844.49987')




intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.guilds = True
s = intents.all()



client = commands.Bot(command_prefix='*', help_command= None)

#conectores
conector = sqlite3.connect('transações.db')
curso = conector.cursor()

#curso.execute("CREATE TABLE transações (id integer, transações text)")




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()


client_status = cycle(['buseta', ' é foda lek','bom dia adm ', 'to triste volta pra mim lili','Vai se fuder serjo seu baitola','buseta pra cima ', 'siga o meu criador no tt imediatamente (@Henrique_clebs)','caraio eu sou virge','sdd dela bixo ','Lili da uma chance pro clebso prf ele só quer te fazer feliz🤝🤝🤝','🤝'])

@tasks.loop(seconds=300)
async def change_status():
    await client.change_presence(activity=discord.Game(next(client_status)))


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 616552616431976480 :
        client.load_extension(f'cogs.{extension}')
        await ctx.reply(f'{extension} carregada')
        print(f'{extension} carregou')
    else :
        await ctx.reply('Você não tem permissão para executar esse comando')


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 616552616431976480:
        client.unload_extension(f'cogs.{extension}')
        await ctx.reply(f'{extension} desligada')
        print(f'{extension} desligada')
    else :
        await ctx.reply('Você não tem permissão paar executar esse comando')


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 616552616431976480 :
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.reply(f'{extension} recarregada')
    else : 
        await ctx.reply('Você não tem permissão para executar esse comando')
    


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

    
    
   #comandos 
@client.command()
async def userinfo(ctx, member : discord.User):
    
   
    embed1 = discord.Embed(title = f'Userinfo de {member.name}{member.discriminator}', colour = discord.Colour.purple())
    embed1.add_field(name = 'User:' , value=member.name, inline= False)
    embed1.add_field(name = 'Id:', value=member.id , inline= False)
    embed1.add_field(name = 'Avatar', value = ':', inline= False)
    embed1.set_image(url =member.avatar_url)
    embed1.set_footer(icon_url = ctx.author.avatar_url , text = f'Requisitado por {ctx.author.name}')
    await ctx.reply(embed = embed1)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error , commands.MissingRequiredArgument):
        embed2 = discord.Embed(title = f'Userinfo de {ctx.author.name}{ctx.author.discriminator}', colour = discord.Colour.dark_purple())
        embed2.add_field(name ='User:', value= ctx.author.name , inline= False)
        embed2.add_field(name = 'Id:' , value=ctx.author.id , inline= False)
        embed2.add_field(name = 'Avatar', value = ':' , inline= False)
        embed2.set_image(url =ctx.author.avatar_url)
        embed2.set_footer(icon_url= ctx.author.avatar_url , text = f'Requisitado por {ctx.author.name}')
        await ctx.reply(embed = embed2)

    if isinstance(error , commands.MemberNotFound):
        await ctx.reply(f'Não consegui encontrar um usuario chamado {error}')
    
@client.command()
async def avatar(ctx, member : discord.User):
    av = ctx.author.avatar_url
    embed = discord.Embed(title = f'Avatar de {member}' , cor = discord.Colour.green())
    embed.set_image(url =member.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url , text = f'Requisitado por {ctx.author.name}')
    await ctx.reply(f'{ctx.author.mention}',embed = embed)

@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error , commands.MissingRequiredArgument):
        av = ctx.author.avatar_url
        embed2 = discord.Embed(title = f'Avatar de {ctx.author.name}' , cor = discord.Colour.green())
        embed2.set_image(url= av)
        embed2.set_footer(icon_url= av, text=f'Requisitado por {ctx.author.name}' )
        await ctx.reply(f'{ctx.author.mention}',embed = embed2)

@client.command()
async def ship(ctx, user : discord.User, user_2 :discord.member):
    amor = random.randint(0,100)
    if amor == 100 :
        barra = '[███████████]'
        text = 'Parece que vcs foramm feitos um para o outro'
    if amor >= 70 < 99 :
        barra = '[█████████..]'
        text = 'hmm mas que bela esposa vc tem em '
    if amor >= 50 < 70 :
        barra = '[█████.....]'
        text = 'Até que pode dar certo'
    if amor >= 30 < 50 :
        barra = '[████......]'  
        text = 'oh'  
    if amor  >=10 < 30 :
        barra = '[██........]'
        text = f'bem , isso é bem dificil {ctx.author.mention} mas vc consegue'
    if amor <10 :
        barra = '[█..........]'
        text = 'Não desista amigão'

    embed = discord.Embed(title =barra, descrpition = text, colour = discord.Colour.red())
    embed.set_footer(icon_url= ctx.author.avatar_url , text = f'Requisitado por {ctx.author.name}')
    embed.set_thumbnail(url = user.avatar_url)
    embed.set_thumbnail(url = user_2.avatar_url)
    await ctx.reply(f'{ctx.author.mention}',embed = embed)

@ship.error
async def ship_error(ctx, error):
    if isinstance(error , commands.MissingRequiredArgument):
        await ctx.reply('Não consegui encontrar nenhum usuario com esse nome')

@client.command()
async def help(ctx):
    comandos_adm ='kick\nban'
    comandos='mdf\nmdb\ncalc\navatar\ndata\ntarduzir\nuserinfo\ntapa\nsamba\nsuporte\ndadop\ndado\nsay\nsoun\nroll\ninvite'
    comandos_dinh = 'daily\npagar\napostar\nsaldo'
    embed= discord.Embed(title =f'Ajuda do {client.user}', colour = discord.Colour.green())
    embed.set_thumbnail(url =  ctx.author.avatar_url)
    embed.add_field(name = 'Comandos_geral :', value = comandos,inline= True)
    embed.add_field(name = 'Comandos de ki-coins' ,value =comandos_dinh, inline = False)
    embed.add_field(name = 'Comandos administrativos', value= comandos_adm, inline= False)
    embed.set_footer(icon_url= ctx.author.avatar_url , text = f'Requisitado por {ctx.author.name}')
    await ctx.reply(embed = embed)

@client.command()
async def guildinfo(ctx, guild : discord.Guild):
    embed= discord.Embed(title ='Informações da guild/server', colour = discord.Colour.green())
    embed.add_field(name = 'Id' , value = guild.id, inline= True)
    embed.add_field(name = 'Criador do servidor' , value= f'{guild.owner.name}\n{(guild.owner_id)}',inline= True)
    data_server = guild.created_at
    conversão_server =f'{data_server.day}/{data_server.month}/{data_server.year}'
    embed.add_field(name = 'Servidor criado em ', value = conversão_server, inline= True)
    embed.add_field(name = 'Maior número de membros :', value = guild.max_members, inline=True )
    embed.set_thumbnail(url = guild.icon_url)
    embed.set_footer(icon_url= ctx.author.avatar_url , text = f'Requisitado por {ctx.author.name}')
    await ctx.reply(ctx.author.mention, embed = embed)

@client.command()
async def iconserver(ctx, guild  : discord.Guild):
    embed= discord.Embed(title =f'Icone do servidor {guild.name}')
    embed.set_image(url = guild.icon_url)
    embed.set_footer(icon_url= ctx.author.avatar_url , text = f'Requisitado por {ctx.author.name}')
    await ctx.reply(ctx.author.mention, embed = embed)

@client.command()
async def tamanho(ctx):
    await ctx.reply(f"Sua mensagem tem {len(ctx.message.content)} caracteres")

@client.command()
async def maiuscula(ctx,*, args):
    await ctx.reply(args.upper)

@client.command()
async def minuscula(ctx,*, args):
    await ctx.reply(args.lower)

@client.command()
async def lembrar(ctx, quantidade, tempo, o_que_vc_vai_fazer):
    if tempo == 'minutos':
        temporizador = quantidade * 60
        time.sleep(temporizador)
        embed = discord.Embed(title =f'{ctx.author.mention} chegou a hora de {o_que_vc_vai_fazer}!!!' , colour = discord.
Colour.dark_orange())
        await ctx.reply(embed = embed)
    if tempo == 'horas':
        temp = quantidade * 1440
        time.sleep(temp)
        embed4 = discord.Embed(title =f'{ctx.author.mention} chegou a hora de {o_que_vc_vai_fazer}!!!' , colour = discord.
Colour.blurple())
        await ctx.reply(embed = embed4)

#parte administartiva

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member :discord.Member = None,*, reason = None):
    embed= discord.Embed(title ='Banido',description = member.name, cor = discord.Colour.red())
    embed.add_field(name='Motivo', value = reason)
    embed.set_footer(icon_url= ctx.author.avatar_url , text = f'Banido por {ctx.author.name}')
    await member.ban(reason = reason)
    await member.send(embed = embed)
    await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(kick_members= True)
async def kick(ctx, member :discord.Member = None,*, reason = None):
    embed=discord.Embed(title ='Expulso' , description = member.name, cor = discord.Colour.red())
    embed.add_field(name = 'Motivo', value = reason)
    embed.set_footer(icon_url= ctx.author.avatar_url , text = f'Expulso por {ctx.author.name}')
    await member.kick(reason= reason)
    await member.send(embed = embed)
    await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_messages = True)
async def apagar(ctx, quantidade : int ):
    await ctx.channel.purge(quantidade , limit = 100)

    
@client.command()
async def tapa(ctx, member : discord.Member, motivo ):
    
    dano = random.randint(0,100)
    tapas = random.choice(['https://media.tenor.com/images/6dbd997e3e79f21b7841b244833325c0/tenor.gif','https://media.tenor.com/images/c935147064f19e14173e7a173ed8e608/tenor.gif'])
    embed = discord.Embed(title = f'{ctx.author.name} deu um tapa em {member}', colour = discord.Colour.red())
    embed.add_field(name ='Dano:', value = f'{dano}%', inline= True)
    embed.add_field(name = 'Motivo:', value = motivo)
    embed.set_image(url = tapas)
    await ctx.reply(embed = embed)

@tapa.error
async def tapa_error(ctx, error):
    if isinstance(error , commands.MissingRequiredArgument):
        await ctx.reply('Coloque os argumetos validos')



@client.command()
async def samba(ctx, member : discord.Member):
     
    sambas = random.choice(['https://media.tenor.com/images/23231d8cb9eb887bf03ac5ac478594fd/tenor.gif','https://media.tenor.com/images/a173ce971e0ec5e435e64110ea0a4139/tenor.gif'])
    embed = discord.Embed(title = f'O {ctx.author.name} sambou no {member}!!', color =discord.Colour.green())
    embed.set_image(url = sambas)
    await ctx.reply(embed = embed)

@samba.error
async def samba_error(ctx, error):
    if isinstance(error , commands.MissingRequiredArgument):
        await ctx.reply('Coloque os argumentos corretos')



@client.command()
async def say(ctx,*, arg):
    await ctx.reply(arg)

@client.command()
async def soun(ctx,*, perunta):
    resp1= random.choice(['Eu acho que ','Talvez ','Com certeza '])
    resp2= random.choice(['sim','não'])
    await ctx.reply(f'{resp1}{resp2}')


@client.command()
async def dado(ctx):
    dado= random.randint(0,100)
    await ctx.reply(f'O dado caiu no numero')

@client.command(descrpition ='Com esse comando vc tem um dado personaizado pra quando não tiver dado em casa', case_sensitive= True)
async def dadop(ctx, número1 :int, número2: int):
    aleatorio = random.randint(número1,número2)
    await ctx.reply(f'O dado caiu no número {aleatorio}')


@client.command()
async def roll(ctx, número : int):
    num = random.randint(0,número)
    await ctx.reply(f'O número é {num}')



@client.command()
async def calc(ctx, número_1:int, sinal, número_2:int):
    if sinal == '+':
        soma= número_1 + número_2
        await ctx.reply(f'`{soma}`')
    elif sinal == '/':
        divisao = número_1 / número_2
        await ctx.reply(f'`{divisao}`')
    elif sinal == '-':
        sub= número_1 - número_2
        await ctx.reply(f'`{sub}`')
    elif sinal == '*':
        multi = número_1 * número_2
        await ctx.reply(f'`{multi}`')
    elif sinal == '**':
        poten = número_1 ** número_2
        await ctx.reply(f'`{poten}`')
    else :
        await ctx.reply('Por favor insira um sinal válido') 


@client.command()
async def invite(ctx):
    await ctx.reply(f' `Aqui está o meu link de convite para me adicionar no seu servidor`\nhttps://discord.com/api/oauth2/authorize?client_id=746096342518071366&permissions=0&scope=bot')


@client.command()
async def suporte(ctx):
    await ctx.reply(f'Servidor do goku para reportar erros no goku\nhttps://discord.gg/qxFGeUcN4F')


conect = sqlite3.connect('clients.db')
cursor = conect.cursor()
#cursor.execute("CREATE TABLE clients (id integer, money integer, estado_civil text, nome_usuario text)")



@client.command()
@commands.cooldown(1,86400,commands.BucketType.user)
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

            data = date.today()
            hora_exata = datetime.datetime.now()
            hora =hora_exata.hour
            minuto = hora_exata.minute
            segundo = hora_exata.second
            transação_daily=(f'({data}) as ({hora}:{minuto}:{segundo})  recebeu {valor} no daily ')
            curso.execute("INSERT INTO transações (id, transações) VALUES (?, ?)", (ctx.author.id, transação_daily))
            conector.commit()

            await ctx.reply(f'|Parabens {ctx.author.mention} você ganhou {valor}ki-coins!!|\nAgora vc tem {valor_final}ki-coins')
           
    except sqlite3.IntegrityError :
        cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
        dinheiro = cursor.fetchone()
        bom = dinheiro[0]
        valor_final = bom + valor
        cursor.execute("UPDATE clients SET money = '"+str(valor_final)+"' WHERE id = '"+str(ctx.author.id)+"' ")
        conect.commit()
        data = date.today()
        hora_exata = datetime.datetime.now()
        hora =hora_exata.hour
        minuto = hora_exata.minute
        segundo = hora_exata.second
        transação_daily=(f'({data}) as ({hora}:{minuto}:{segundo})  recebeu {valor} no daily ')
        curso.execute("INSERT INTO transações (id, transações) VALUES (?, ?)", (ctx.author.id, transação_daily))
        conector.commit()
        await ctx.reply(f'|Parabens {ctx.author.mention} vc ganhou {valor} ki-coins!!|\nAgora vc tem {valor_final}ki-coins')
        
@daily.error
async def daily_error(ctx, error):
    if isinstance (error, commands.CommandOnCooldown):
        data = date.today()
        hora_exata = datetime.datetime.now()
        hora =hora_exata.hour
        minuto = hora_exata.minute
        segundo = hora_exata.second
        amanhã = data.day + 1
        await ctx.reply(f'Você só poderá pegar seu daily novamente amanhã as{hora}:{minuto}:{segundo}')
        
        
        
        
        
        
        

@client.command(0)
async def pagar(ctx, user : discord.User, valor : int):
    name = f'{user.name}#{user.discriminator}'
    nome = f'{ctx.author.name}#{ctx.author.discriminator}'
    try :
        with conect :
            #adicionando o user caso ele não esteja na tabela 
            valor_inicial = 0
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario ) VALUES (?, ?, ?, ?)",(user.id, valor_inicial, 'solteiro(a)', name))
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(ctx.author.id, valor_inicial, 'solteiro(a)', nome))
            #tirando os ki-coins da conta do author
            cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
            dinheiro = cursor.fetchone()
            sla = dinheiro[0]
            valor_f = sla - valor
            if valor_f < 1 :
                await ctx.reply(f'{ctx.author.mention} você não pode pagar com dinheiro que não tem ')
            else :
                cursor.execute("UPDATE clients SET money = '"+str(valor_f)+"' WHERE id = '"+str(ctx.author.id)+"' ")
                #colocando os ki-coins na conta do user 
                cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
                dinhero = cursor.fetchone()
                samp = dinhero[0]
                val = samp + valor
                cursor.execute("UPDATE clients SET money = '"+str(val)+"' WHERE id = '"+str(user.id)+"' ")
                embed = discord.Embed(title = 'Transação concluida com sucesso!!', colour = discord.Colour.green())
                embed.add_field(name =f'Transação realizada por {ctx.author.name} para {user.name}', value= f'Valor = {valor} ki-coins') 
                embed.set_thumbnail(url = ctx.author.avatar_url)  
                conect.commit()
                #############registro de transação ####################
                data = date.today()
                hora_exata = datetime.datetime.now()
                hora =hora_exata.hour
                minuto = hora_exata.minute
                segundo = hora_exata.second
                transação_daily=(f'({data}) as ({hora}:{minuto}:{segundo})  recebeu {valor} de {ctx.author.name}#{ctx.author.discriminator}')
                curso.execute("INSERT INTO transações (id, transações) VALUES (?, ?)", (ctx.author.id, transação_daily))
                conector.commit()
                #################################
                await ctx.reply(embed = embed)

    except sqlite3.IntegrityError : 
        cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
        dinheiro = cursor.fetchone()
        sla = dinheiro[0]
        valor_f = sla - valor
        if valor_f < 1 :
            await ctx.reply(f'{ctx.author.mention} você não pode pagar com dinheiro que não tem ')
        else :
            cursor.execute("UPDATE clients SET money = '"+str(valor_f)+"' WHERE id = '"+str(ctx.author.id)+"' ")
            cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
            dinhero = cursor.fetchone()
            samp = dinhero[0]
            val = samp + valor
            cursor.execute("UPDATE clients SET money = '"+str(val)+"' WHERE id = '"+str(user.id)+"' ")
            embed = discord.Embed(title = 'Transação concluida com sucesso!!', colour = discord.Colour.green())
            embed.add_field(name =f'Transação realizada por {ctx.author.mention} para {user}', value= f'Valor = {valor} ki-coins') 
            embed.set_thumbnail(url = ctx.author.avatar_url)  
            conect.commit()
            #############registro de transação ####################
            data = date.today()
            hora_exata = datetime.datetime.now()
            hora =hora_exata.hour
            minuto = hora_exata.minute
            segundo = hora_exata.second
            transação_pagamento=(f'({data}) as ({hora}:{minuto}:{segundo})  recebeu {valor} de {ctx.author.name}#{ctx.author.discriminator}')
            curso.execute("INSERT INTO transações (id, transações) VALUES (?, ?)", (ctx.author.id, transação_pagamento))
            conector.commit()
            ###################################
            await ctx.send(ctx.author.mention, embed = embed)


@client.command()
async def saldo(ctx, user : discord.User):
    name = f'{user.name}#{user.discriminator}'
    nome = f'{ctx.author.name}#{ctx.author.discriminator}'
    try :
        with conect :
            valor_inicial = 0
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario ) VALUES (?, ?, ?, ?)",(user.id, valor_inicial, 'solteiro(a)', name))
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(ctx.author.id, valor_inicial, 'solteiro(a)', nome))
            cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
            dinheiro = cursor.fetchone()
            dor = dinheiro[0]
            conect.commit()
            await ctx.reply(f'{ctx.author.mention} {user.name} tem {dor} ki-coins')

    except sqlite3.IntegrityError :
        cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
        dinheiro = cursor.fetchone()
        dor = dinheiro[0]
        await ctx.reply(f'{ctx.author.mention} {user.name} tem {dor} ki-coins')
            
@saldo.error
async def saldo_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
        dinheiro = cursor.fetchone()
        dor = dinheiro[0]
        await ctx.reply(f'{ctx.author.mention} você tem {dor} ki-coins')



@client.command()
async def give(ctx, user : discord.User, valor : int):
    
    name = f'{user.name}#{user.discriminator}'
    if ctx.author.id == 616552616431976480 :
        try :
            with conect :
            
                valor_inicial = 0
                cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario ) VALUES (?, ?, ?, ?)",(user.id, valor_inicial, 'solteiro(a)', name))
                cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
                dinhero = cursor.fetchone()
                samba = dinhero[0]
                val = samba + valor
                cursor.execute("UPDATE clients SET money = '"+str(val)+"' WHERE id = '"+str(user.id)+"' ")
                conect.commit()

        except sqlite3.IntegrityError :
            cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
            dinhero = cursor.fetchone()
            samba = dinhero[0]
            val = samba + valor
            cursor.execute("UPDATE clients SET money = '"+str(val)+"' WHERE id = '"+str(user.id)+"' ")
            conect.commit()
    else :
        pass
    



@client.command()
async def reg(ctx, user : discord.User):
    name = f'{user.name}#{user.discriminator}'
    if ctx.author.id == 616552616431976480 :
        valor_inicial = 0
        cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario ) VALUES (?, ?, ?, ?)",(user.id, valor_inicial, 'solteiro(a)', name))
        conect.commit()
        await ctx.reply('sagygf')
    else :
        pass

@client.command()
async def aposta(ctx, user : discord.User, valor : int):
    try :
        with conect :
            valor_inicial = 0
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(ctx.author.id, valor_inicial, 'solteiro', f'{ctx.author.name}#{ctx.author.discriminator}'))
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(user.id, valor_inicial, 'solteiro', f'{user.name}#{user.discriminator}'))
            cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
            num = cursor.fetchone()
            nom = num[0]

            cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
            dinhero = cursor.fetchone()
            samba = dinhero[0]
            if nom < 1 :
                await ctx.reply(f'{ctx.author.mention} você não pode apostar um quantia que não tem ')
            elif samba < 1 :
                await ctx.reply(f' O {user.name} não tem {valor} ki-coins ')
            else :
                apost= f'{user.mention}, {ctx.author.mention} quer fazer uma aposta no cara ou coroa com você\nno valor de {valor} ki-coins , aceita a aposta ( :white_check_mark: ) ou vai amarelar (:x:) , para fazer a aposta os dois devem clicar em (✅)  ' 
                
                a = await ctx.send(apost)
                await a.add_reaction('✅')
                await a.add_reaction('❌')

                def check(reaction, user ):
                    return user == user and str(reaction.emoji) == '✅'
                def check_2(reaction, ctx ):
                    return ctx.author == ctx.author and str(reaction.emoji) == '✅'
                    
                     

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                    reaction, ctx.author = await client.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    pass
                else:
                    #aposta do user
                    cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
                    dinhero = cursor.fetchone()
                    samba = dinhero[0]
                    valor_user = samba - valor
                    cursor.execute("UPDATE clients SET money = '"+str(valor_user)+"' WHERE id = '"+str(user.id)+"' ")
                    conect.commit()
                    #aposta do author  ctx 
                    cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
                    dinh = cursor.fetchone()
                    valo = dinh[0]
                    valor_author =  valo - valor
                    cursor.execute("UPDATE clients SET money = '"+str(valor_author)+"' WHERE id = '"+str(ctx.author.id)+"' ")
                    conect.commit()
                    ##############################
                    quantia = valor * 2
                    escolha = random.choice([ctx.author.id, user.id])
                    await ctx.send(f'Parabens <@{escolha}> você ganhou {quantia} ki-coins, ')
                    cursor.execute("SELECT money FROM clients WHERE id = '"+str(escolha)+"'")
                    dindin = cursor.fetchone()
                    cu = dindin[0]
                    valor_porraaaa = cu + quantia
                    cursor.execute("UPDATE clients SET money = '"+str(valor_porraaaa)+"' WHERE id = '"+str(escolha)+"' ")
                    conect.commit()
                    #############registro de transação ####################
                    data = date.today()
                    hora_exata = datetime.datetime.now()
                    hora =hora_exata.hour
                    minuto = hora_exata.minute
                    segundo = hora_exata.second
                    transação_aposta=(f'({data}) as ({hora}:{minuto}:{segundo})  recebeu {valor} de {ctx.author.name}#{ctx.author.discriminator} em uma aposta')
                    curso.execute("INSERT INTO transações (id, transações) VALUES (?, ?)", (ctx.author.id, transação_aposta))
                    conector.commit()
                    #####################################


    except sqlite3.IntegrityError :
        cursor.execute("INSERT INTO clients (estado_civil, nome_usuario) VALUES (?, ?)",('solteiro', f'{ctx.author.name}#{ctx.author.discriminator}'))
        cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
        num = cursor.fetchone()
        nom = num[0]
        cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
        dinhero = cursor.fetchone()
        samba = dinhero[0]
        if nom < 1 :
            await ctx.reply(f'{ctx.author.mention} você não pode apostar um quantia que não tem ')
        elif samba < 1 :
            await ctx.reply(f'{user.mention} você não pode apostar uma quantia que não tem ')
        else :
            apost= f'{user.mention}, {ctx.author.mention} quer fazer uma aposta com você\nno valor de{valor} ki-coins , aceita a aposta ( :white_check_mark: ) ou vai amarelar (:x:) ? ' 
            a = await ctx.send(apost)
            await a.add_reaction('✅')
            await a.add_reaction('❌')
            def check(reaction, user ):
                return user == user and str(reaction.emoji) == '✅'
            def check_2(reaction, ctx ):
                return ctx.author == ctx.author and str(reaction.emoji) == '✅'
        
        
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                reaction, ctx.author = await client.wait_for('reaction_add', timeout=60.0, check=check_2)
            except asyncio.TimeoutError:
                pass
            else :
                cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
                dinhero = cursor.fetchone()
                samba = dinhero[0]
                valor_user = samba - valor
                cursor.execute("UPDATE clients SET money = '"+str(valor_user)+"' WHERE id = '"+str(user.id)+"' ")
                conect.commit()
                #aposta do author  ctx 
                cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
                dinh = cursor.fetchone()
                valo = dinh[0]
                valor_author =  valo - valor
                cursor.execute("UPDATE clients SET money = '"+str(valor_author)+"' WHERE id = '"+str(ctx.author.id)+"'")
                conect.commit()
                ##############################
                quantia = valor * 2
                escolha = random.choice([ctx.author.id, user.id])
                await ctx.send(f'Parabens <@{escolha}> você ganhou {quantia} ki-coins, ')
                
                dindin = cursor.fetchone()
                cu = dindin[0]
                valor_porraaaa = cu + quantia
                cursor.execute("UPDATE clients SET money = '"+str(valor_porraaaa)+"' WHERE id = '"+str(escolha)+"' ")
                #############registro de transação ####################
                data = date.today()
                hora_exata = datetime.datetime.now()
                hora =hora_exata.hour
                minuto = hora_exata.minute
                segundo = hora_exata.second
                transação_aposta=(f'({data}) as ({hora}:{minuto}:{segundo})  recebeu {valor} de {ctx.author.name}#{ctx.author.discriminator} em uma aposta')
                curso.execute("INSERT INTO transações (id, transações) VALUES (?, ?)", (ctx.author.id, transação_aposta))
                conector.commit()




@client.event
async def on_member_join(member):
    try :
        with conect :
            name = f'{member.name}#{member.discriminator}'
            valor_inicial = 0
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(member.id, valor_inicial, 'solteiro(a)', name))
    except sqlite3.IntegrityError :
        pass

@client.command()
async def casar(ctx, user : discord.User):
    name = f'{user.name}#{user.discriminator}'
    nome = f'{ctx.author.name}#{ctx.author.discriminator}'
    valor_inicial = 0
    try :
        with conect :
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(user.id, valor_inicial, 'solteiro(a)', name))
            cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(ctx.author.id, valor_inicial, 'solteiro(a)', nome))
            cursor.execute("SELECT estado_civil FROM clients WHERE id = '"+str(user.id)+"'")
            a = cursor.fetchone()
            b = a[0]
            if b.startswith('casado') :
                await ctx.reply(f'{ctx.author.mention} o {user.mention} já é {b}')
            else :
                cursor.execute("SELECT estado_civil FROM clients WHERE id = '"+str(ctx.author.id)+"'")
                c = cursor.fetchone()
                d = c[0]
                if d.startswith('casado'):
                    await ctx.reply(f'{ctx.author.mention} você já é {d}')
                else : 
                    a = await ctx.send(f'{user.mention} ,{ctx.author.mention} quer se casar com você , aceitas ou vai dar um fora no(a) coitado(a) ? ,\n para aceitar o casamento os dois devem clicar em (✅)')
                    await a.add_reaction('✅')
                    await a.add_reaction('❌')
                    def check(reaction, user ):
                        return user == user and str(reaction.emoji) == '✅'
                    def check_2(reaction, ctx ):
                        return ctx.author == ctx.author and str(reaction.emoji) == '✅'
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                        reaction, ctx.author = await client.wait_for('reaction_add', timeout=60.0, check=check_2)
                    except asyncio.TimeoutError:
                        pass

                    else : 
                        await ctx.send(f'Parabens {user.mention} e {ctx.author.mention} vocês se casaram , felicidades ao casal' )
                        casado_user = f'casado com {ctx.author.name}#{ctx.author.discriminator}'
                        cursor.execute("UPDATE clients SET estado_civil = '"+str(casado_user)+"' WHERE id = '"+str(user.id)+"' ")
                        casado_author = f'casado com {user.name}#{user.discriminator}'
                        cursor.execute("UPDATE clients SET estado_civil = '"+str(casado_author)+"' WHERE id = '"+str(ctx.author.id)+"'")
                        conect.commit()

    except sqlite3.IntegrityError :

        cursor.execute("SELECT estado_civil FROM clients WHERE id = '"+str(user.id)+"'")
        a = cursor.fetchone()
        b = a[0]
        if b.startswith('casado') :
            await ctx.reply(f'{ctx.author.mention} o {user.mention} já é {b}')
        else :
            cursor.execute("SELECT estado_civil FROM clients WHERE id = '"+str(ctx.author.id)+"'")
            c = cursor.fetchone()
            d = c[0]
            if d.startswith('casado'):
                await ctx.reply(f'{ctx.author.mention} você já é {d}')
            else : 
                a = await ctx.send(f'{user.mention} ,{ctx.author.mention} quer se casar com você , aceitas ou vai dar um fora no(a) coitado(a) ? , para aceitar o casamento os dois devem clicar em (✅)')
                await a.add_reaction('✅')
                await a.add_reaction('❌')

                def check(reaction, user ):
                    return user == user and str(reaction.emoji) == '✅'
                def check_2(reaction, ctx ):
                    return ctx.author == ctx.author and str(reaction.emoji) == '✅'
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                    reaction, ctx.author = await client.wait_for('reaction_add', timeout=60.0, check=check_2)
                except asyncio.TimeoutError:
                    pass
                else : 
                    await ctx.send(f'Parabens {user.mention} e {ctx.author.mention} vocês se casaram , felicidades ao casal' )
                    casado_user = f'casado com {ctx.author.name}#{ctx.author.discriminator}'
                    cursor.execute("UPDATE clients SET estado_civil = '"+str(casado_user)+"' WHERE id = '"+str(user.id)+"' ")
                    casado_author = f'casado com {user.name}#{user.discriminator}'
                    cursor.execute("UPDATE clients SET estado_civil = '"+str(casado_author)+"' WHERE id = '"+str(ctx.author.id)+"'")
                    conect.commit()

@client.command()
@commands.cooldown(1,30,commands.BucketType.user)
async def perfil(ctx, user : discord.User):
    cursor.execute("SELECT estado_civil FROM clients WHERE id = '"+str(user.id)+"'")
    esta = cursor.fetchone()
    estad = esta[0]
    cursor.execute("SELECT money FROM clients WHERE id = '"+str(user.id)+"'")
    din = cursor.fetchone()
    dinheiro = din[0]
    embed = discord.Embed(title =f'Perfil de {user.name}', cor = discord.Colour.green())
    embed.add_field(name ='Saldo', value = f'{dinheiro} ki-coins', inline= True)
    embed.add_field(name = 'Estado civíl', value = f'{estad}', inline= True)
    embed.set_thumbnail(url =user.avatar_url)
    await ctx.reply(embed = embed)

@perfil.error
async def perfil_error(ctx, error):
    
    cursor.execute("SELECT estado_civil FROM clients WHERE id = '"+str(ctx.author.id)+"'")
    c = cursor.fetchone()
    d = c[0]

    
    name = f'{ctx.author.name}#{ctx.author.discriminator}'
    cursor.execute("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)",(ctx.author.id, d, 'solteiro(a)', name))
    
    cursor.execute("SELECT estado_civil FROM clients WHERE id = '"+str(ctx.author.id)+"'")
    esta = cursor.fetchone()
    estad = esta[0]
    cursor.execute("SELECT money FROM clients WHERE id = '"+str(ctx.author.id)+"'")
    din = cursor.fetchone()
    dinheiro = din[0]
    embed = discord.Embed(title =f'Perfil de {ctx.author.name}', cor = discord.Colour.green())
    embed.add_field(name ='Saldo', value = f'{dinheiro} ki-coins', inline= True)
    embed.add_field(name = 'Estado civíl', value = f'{estad}', inline= True)
    embed.set_thumbnail(url =ctx.author.avatar_url)
    await ctx.reply(embed = embed)

@client.command()
async def transações(ctx, user : discord.User):
    curso.execute("SELECT transações FROM transações WHERE id = '"+str(ctx.author.id)+"'")
    tranct = curso.fetchall()

    embed = discord.Embed(title =f'Transações de {user.name}', colour = discord.Colour.random())
    a = len(tranct)
    if a > 10 :
        mostrar = tranct[0:10]
        vali = 0
        while vali < 10 :
            embed.add_field(name = f'{str(mostrar[0])}', value= None)
            embed.add_field(name = f'{str(mostrar[1])}', value= None)
            embed.add_field(name = f'{str(mostrar[2])}', value= None)
            embed.add_field(name = f'{str(mostrar[3])}', value= None)
            embed.add_field(name = f'{str(mostrar[4])}', value= None)
            embed.add_field(name = f'{str(mostrar[5])}', value= None)
            embed.add_field(name = f'{str(mostrar[6])}', value= None)
            embed.add_field(name = f'{str(mostrar[7])}', value= None)
            embed.add_field(name = f'{str(mostrar[8])}', value= None)
            embed.add_field(name = f'{str(mostrar[9])}', value= None)
            embed.add_field(name = f'{str(mostrar[10])}', value= None)
            await ctx.reply(embed = embed)


            '''
            embed.add_reaction('✅')
            embed.add_reaction('❌')
           
           

           
            def check (reaction, ctx ):
                return ctx.author == ctx.author and str(reaction.emoji) == '✅'

            try :
                reaction, ctx.author = await client.wait_for('reaction_add', timeout=60.0, check = check)

            except asyncio.TimeoutError:
                pass

            else :
                ...
                #editar a mensagem e enviar uma nova embed 

            '''


@client.event
async def on_guild_join(guild):
    async for member in guild.fetch_members(limit = None) :
        a = [(member.id , 0, 'solteiro(a)', f'{member.name}#{member.discriminator}')]
        cursor.executemany("INSERT INTO clients (id, money, estado_civil, nome_usuario) VALUES (?, ?, ?, ?)", (a))
        conect.commit()




            
        
      
      
      
      
      
      
      
      
      
      
       
        
        
        
        
        
        




    





















    









                

        






client.run('Token')

























