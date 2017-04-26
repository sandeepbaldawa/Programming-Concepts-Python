# replace all *.t by *.txt
find . -name "*.t" -execdir rename  's/.t/.txt/' '{}' \;
