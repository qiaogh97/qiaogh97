day=23

year=2026
month=04
week=03

day_num=${year}${month}${day}

# day
cp ../notion/time/png/new_${day_num}*.png ./png/.
ls -lh ./png/new_${day_num}*.png

# week
#cp ../notion/time/png/${year}${month}week${week}_table.png ./png/.
#cp ../notion/time/png/${year}${month}week${week}_emotion.png ./png/.
#cp ../notion/time/png/${year}${month}week${week}_location_pie.png ./png/.
#ls -lh ./png/${year}${month}week${week}_*.png

# month
#cp ../notion/time/png/${year}${month}_pie.png ./png/.
#cp ../notion/time/png/${year}${month}_location_pie.png ./png/.
#cp ../notion/time/png/${year}${month}_work_time.png ./png/.
#ls -lh ./png/${year}${month}*.png
