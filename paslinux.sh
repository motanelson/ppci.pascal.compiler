python3 -m ppci pascal  $1 -o $1.o  --machine x86_64 
python3 -m ppci objcopy $1.o $1.elf --output-format elf