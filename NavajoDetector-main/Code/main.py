import csv
from data_loader import load_navajo_sentences
from language_detection import create_client, batch_detect_languages, translate_round_trip

def main():
    file_path = 'navajo10k.txt'
    navajo_sentences = load_navajo_sentences(file_path)
    output_file = 'translation_output.csv'
    client = create_client()  # Create a single Translate client

    # Process all sentences at once
    languages_and_confidences = batch_detect_languages(client, navajo_sentences[:10000])

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Navajo Sentence', 'Detected Language', 'Confidence', 'Translation to English', 'Back Translation'])

        for i, (language, confidence) in enumerate(languages_and_confidences):
            sentence = navajo_sentences[i]
            if language != 'unknown':  # Check if the language was detected
                translated_to_english, translated_back = translate_round_trip(client, sentence, language)
                writer.writerow([sentence, language, confidence, translated_to_english, translated_back])
            else:
                writer.writerow([sentence, 'unknown', 0, 'N/A', 'N/A'])

if __name__ == "__main__":
    main()
