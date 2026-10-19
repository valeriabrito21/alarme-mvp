import time
from datetime import datetime, timedelta

INTERVALO_MINUTOS = 30      # ajuste: quanto tempo entre avisos
DURACAO_TOTAL_HORAS = None # ex.: 2 para durar 2h, ou None para infinito

TEMPO_ATUALIZACAO_SEG = 30 # atualiza a contagem regressiva a cada 30s
ARQUIVO_LOG = "log.txt"


def agora_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def registrar_log(msg: str):
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{agora_str()}] {msg}\n")


def main():
    intervalo = INTERVALO_MINUTOS * 60  # segundos
    atualizacao = max(1, TEMPO_ATUALIZACAO_SEG)

    inicio = datetime.now()
    fim = None
    if DURACAO_TOTAL_HORAS is not None:
        fim = inicio + timedelta(hours=DURACAO_TOTAL_HORAS)

    print("🥤 Beber água por intervalo (com contagem regressiva)")
    print(f"Intervalo: {INTERVALO_MINUTOS} minutos")
    if fim:
        print(f"Duração total: {DURACAO_TOTAL_HORAS} horas (termina em: {fim.strftime('%H:%M')})")
    else:
        print("Duração total: infinito (CTRL+C para parar)")
    print("-" * 50)

    proximo = time.time() + intervalo

    try:
        while True:
            if fim and datetime.now() >= fim:
                print("\n✅ Fim da duração. Até a próxima!")
                registrar_log("Programa encerrado por duração total.")
                break

            segundos_restantes = proximo - time.time()

            # Se ainda não chegou a hora, mostramos contagem
            if segundos_restantes > 0:
                minutos_restantes = int(segundos_restantes // 60)
                secs = int(segundos_restantes % 60)

                # mostra update a cada ~30s (mas sem exagerar)
                print(f"\r⏳ Faltam {minutos_restantes:02d}:{secs:02d} para a próxima água.", end="")
                time.sleep(min(atualizacao, segundos_restantes))
                continue

            # Hora do aviso (dispara uma vez)
            msg = "💧 Hora da água!"
            print("\n" + msg)
            registrar_log(msg)

            # Agenda o próximo
            proximo = time.time() + intervalo

    except KeyboardInterrupt:
        print("\n🛑 Interrompido pelo usuário (CTRL+C).")
        registrar_log("Programa interrompido pelo usuário.")


if __name__ == "__main__":
    main()