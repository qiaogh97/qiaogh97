day=20

year=2025
month=04
week=03

day_num=${year}${month}${day}

# day
cp ../notion/time/png/new_${day_num}*.png ./png/.
ls -lh ./png/new_${day_num}*.png

# week
#cp ../notion/time/png/${year}${month}week${week}_*show.png ./png/.
#ls -lh ./png/${year}${month}week${week}_*show.png

# month
#cp ../notion/time/png/${year}${month}_pie.png ./png/.
#cp ../notion/time/png/${year}${month}_work_time.png ./png/.
#ls -lh ./png/${year}${month}*.png
