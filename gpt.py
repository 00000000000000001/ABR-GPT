from openai import OpenAI
import datetime
import config


def send_message(text, instructions=""):
    try:
        client = OpenAI(api_key=config.API_KEY)

        assistant = client.beta.assistants.retrieve(assistant_id=config.ASS_KEY)

        thread = client.beta.threads.create()

        client.beta.threads.messages.create(thread_id=thread.id, role="user", content=text)

        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions=instructions,
        )

        while run.status != "completed":
            keep_retrieving_run = client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id
            )
            # Aktuelle Uhrzeit holen und formatieren
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Statusmeldung mit Uhrzeit ausgeben
            print(f"{current_time} - Run status: {keep_retrieving_run.status}")

            if keep_retrieving_run.status == "completed":
                break
            if keep_retrieving_run.status == "failed":
                return None

        messages = client.beta.threads.messages.list(thread_id=thread.id)

        return messages.data[0].content[0].text.value
    except:
        raise Exception("Fehler beim Verbindungsaufbau mit OpenAI. Bitte überprüfen Sie ob API-Key und ASST-Key vorliegen und das Sie mit dem Internet verbunden sind.")
