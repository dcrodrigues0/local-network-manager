#!/bin/zsh
chmod 777 ./run.sh
while :
  do
processo=`ps ax | grep "flask" | grep -v grep| wc -l`
X=`find "/home/luke/PycharmProjects/py-homeNetwork-control/app.py" -cmin -5`
if [ !  -z "$X" ]; then
  kill -9 $(pgrep flask)
  zsh ./flaskStart.sh & #ESSA PORRA QUANDO COMEÇA A RODAR NÃO PARA DESGRAÇA
fi
sleep 5
done