# 🥤 Beber água por intervalo (Console MVP)

Um mini projeto em Python que te lembra de beber água em **intervalos regulares**.
Funciona no **console**, mostra uma **contagem regressiva** e registra cada lembrete em um arquivo `log.txt`.

---

## ✨ Funcionalidades
- 🕒 Dispara um lembrete a cada `INTERVALO_MINUTOS`
- ⏳ Mostra contagem regressiva no terminal
- 📝 Grava um log em `log.txt` com o horário de cada lembrete
- ⏻ Para com **CTRL+C** (ou finaliza automaticamente se `DURACAO_TOTAL_HORAS` for definido)

---

## ⚙️ Configurações (no código)
Abra `src/main.py` e ajuste:

- `INTERVALO_MINUTOS = 30`
  - intervalo entre lembretes
- `DURACAO_TOTAL_HORAS = None`
  - defina um número (ex.: `2`) para parar automaticamente após esse tempo
- `TEMPO_ATUALIZACAO_SEG = 30`
  - frequência com que a contagem regressiva é atualizada no console
- `ARQUIVO_LOG = "log.txt"`
  - arquivo onde os lembretes serão registrados

---

## ▶️ Como executar
1. Entre na pasta do projeto `alarme-mvp`
2. Rode o comando:

```bat
python src\main.py