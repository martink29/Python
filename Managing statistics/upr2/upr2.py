import matplotlib.pyplot as plt
import csv

text = "The main visible effect (in longitude) of the variation of the Moon is that during the course of every month, at the octants of the Moon's phase that follow the syzygies (i.e. halfway between the new or the full moon and the next-following quarter), the Moon is about two thirds of a degree farther ahead than would be expected on the basis of its mean motion (as modified by the equation of the centre and by the evection). But at the octants that precede the syzygies, it is about two thirds of a degree behind. At the syzygies and quarters themselves, the main effect is on the Moon's velocity rather than its position.In 1687 Newton published, in the 'Principia', his first steps in the gravitational analysis of the motion of three mutually-attracting bodies. This included a proof that the Variation is one of the results of the perturbation of the motion of the Moon caused by the action of the Sun, and that one of the effects is to distort the Moon's orbit in a practically elliptical manner (ignoring at this point the eccentricity of the Moon's orbit), with the centre of the ellipse occupied by the Earth, and the major axis perpendicular to a line drawn between the Earth and Sun. The Variation has a period of half a synodic month and causes the Moon's ecliptic longitude to vary by nearly two-thirds of a degree, more exactly by +2370sin(2D) where D is the mean elongation of the Moon from the Sun.The variational distortion of the Moon's orbit is a different effect from the eccentric elliptical motion of a body in an unperturbed orbit. The Variation effect would still occur if the undisturbed motion of the Moon had an eccentricity of zero (i.e. circular). The eccentric Keplerian ellipse is another and separate approximation for the Moon's orbit, different from the approximation represented by the (central) variational ellipse. The Moon's line of apses, i.e. the long axis of the Moon's orbit when approximated as an eccentric ellipse, rotates once in about nine years, so that it can be oriented at any angle whatever relative to the direction of the Sun at any season. (The angular difference between these two directions used to be referred to, in much older literature, as the annual argument of the Moon's apogee.) Twice in every period of just over a year, the direction of the Sun coincides with the direction of the long axis of the eccentric elliptical approximation of the Moon's orbit (as projected on to the ecliptic)."

text = text.lower()

counts = {}

for char in text:
    if 'a' <= char <= 'z':
        counts[char] = counts.get(char, 0) + 1

total_letters = sum(counts.values())

letters = sorted(counts.keys())
values = [counts[letter] for letter in letters]
percentages = [(counts[letter] / total_letters) * 100 for letter in letters]

with open("letter_counts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Letter", "Count", "Percentage"])
    
    for letter in letters:
        percent = counts[letter] / total_letters * 100
        writer.writerow([letter, counts[letter], f"{percent:.2f}%"])

plt.bar(letters, values)
plt.title("Letter Frequency in Text")
plt.xlabel("Letters")
plt.ylabel("Count")

for i in range(len(letters)):
    plt.text(i, values[i] + 1, f"{values[i]} ({percentages[i]:.1f}%)", ha='center')

plt.show()