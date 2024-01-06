from openai import OpenAI

client = OpenAI(
    api_key="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",
)

# Prompt-Tools:
# https://easy-peasy.ai/de/templates/chatgpt-prompt-generator
# https://neuralwriter.com/de/prompt-tool/


def abr_gpt(string):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Als Experte für medizinische Fachtexte, sollen Sie einen Arztbrief erstellen. Geben Sie bitte nur den Hauptteil mit den medizinischen Informationen an, ohne Anrede, Grußformel oder ähnliches. Der Hauptteil sollte in einzelne Abschnitte unterteilt sein, die jeweils eine präzise Überschrift haben. Stellen Sie sicher, dass der Arztbrief alle relevanten medizinischen Details enthält, einschließlich der Diagnose, des Behandlungsverlaufs, der verschriebenen Medikamente und möglicher Empfehlungen für den Patienten. Die Informationen sollten klar und verständlich formuliert sein, damit andere medizinische Fachleute den Arztbrief problemlos lesen und verstehen können. Achten Sie darauf, dass alle medizinischen Abkürzungen ausgeschrieben und erläutert werden, um Missverständnisse zu vermeiden.",
            },
            {"role": "user", "content": string},
        ],
    )

    return completion.choices[0].message.content
