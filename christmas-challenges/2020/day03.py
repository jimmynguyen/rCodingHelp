# I wish for a white christmas... (Day 3)
# Challenge :
# Write a program that shows a snowman on the screen!
import random
import sys
import time

for i in range(5):
  print(f"a snowman on the screen{('.' * i)}")
  if i < 4:
    sys.stdout.write("\033[F")
  time.sleep(1)

# https://www.asciiart.eu/holiday-and-events/christmas/snowmen
ascii_img = ".      *    *           *.       *   .                      *     .\n" \
  + "               .   .                   __   *    .     * .     *\n" \
  + "    *       *         *   .     .    _|__|_        *    __   .       *\n" \
  + "  .  *  /\       /\          *        ('')    *       _|__|_     .\n" \
  + "       /  \   * /  \  *          .  <( . )> *  .       ('')   *   *\n" \
  + "  *    /  \     /  \   .   *       _(__.__)_  _   ,--<(  . )>  .    .\n" \
  + "      /    \   /    \          *   |       |  )),`   (   .  )     *\n" \
  + "   *   `||` ..  `||`   . *.   ... ==========='`   ... '--`-` ... *"

for i in range(10):
  ascii_img = ascii_img.replace("*"," ")
  for j in range(28):
    n = random.randint(0,len(ascii_img)-1)
    if ascii_img[n] == " ":
      ascii_img = ascii_img[:n] + "*" + ascii_img[n+1:]
  print(ascii_img)
  if i < 9:
    sys.stdout.write("\033[8F")
  time.sleep(1)
