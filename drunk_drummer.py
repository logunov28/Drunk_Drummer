from mido import Message, MidiFile, MidiTrack, second2tick

# Получаем дорожку ударных в виде списка вида ([Message('note_on', channel=0, note=38, velocity=46, time=203), ...
path_to_mid = input("Вставьте путь к mid-файлу с ударными:")[1:-1]
drums = MidiFile(path_to_mid)

# Для проверки
#print (drums)
#x = input()