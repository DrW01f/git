"""
git config --global user.email "ВАШ email"
git config --global user.name "ВАШЕ Имя"
git remote add origin https://github.com/DrW01f/Test.git
git branch -M main
git push -u origin main
git push  --set-upstream origin description
git push origin --delete <branch_name>

git --version       # версия git
git remote -v       #
git status          #
git log             # показывает подробную историю коммитов (с датой-временем, автором, текстом коммита)
git log --oneline   # показывает историю кратко в 1 строку
git log --graph

git init                        # создание папки с git
git add file_name               # добавление файла в отслеживание git (без имени добавит все файлы)
git rm --cached file_name       # удаляет файл из отслеживания git

git commit -m "commit_text"     # добавление коммита с комментарием
git commit -a                   # git add + git commit
git commit -am                  # git add + git commit "commit_text"

git restore file_name           # отмена коммита для файла (откат на предыдущий)

git checkout hash_commit        #
git diff    #

git reset hash_commit           #
git reset --hard hash_commit    # отмена коммита (без указания хэша сбрасывает до последнего коммита)
git revert hash_commit          # не отменяет, а добавляеет новый коммит, отменеяющий старый

git reflog      # история всех операций (в т. ч. отмена коммитов, переходы по истории, создание новых )

git branch                      # список веток в репозитории
git branch name_branch          # создание новой ветки с именем name_branch
git branch -d name_branch       # безопасное удаление ветки

ssh_keygen          # создание ключа





main branch !!!!!!!!!!!!


this is no info in main branch


"""