# REQUIREMENTS = 'Level: 20'
# REQUIREMENTS = 'Level: 10 ===AND=== Level: 20'
# REQUIREMENTS = 'Level: 10 ===AND=== Level: 20 ===AND=== Level: 30'
# REQUIREMENTS = 'Level: 10 ===OR=== Level: 20'
# REQUIREMENTS = 'Level: 10 ===OR=== Level: 20 ===OR=== Level: 30'
REQUIREMENTS = 'Level: 10 ===OR=== Level: 20 ===AND=== Level: 30 ===OR=== Level: 40'

def print_requirements(requirements, level):
  relation = ''
  indentation = ''.join(['\t'] * level)
  # print(indentation)

  arr = requirements.split(' ===AND=== ')
  # print(arr)
  if (len(arr) == 1):
    arr = requirements.split(' ===OR=== ')
    if (len(arr) == 1):
      print(f"{indentation}{requirements}")
      return
    else:
      relation = 'OR'
  else:
    relation = 'AND'

  for i in range(0, len(arr)):
    print_requirements(arr[i], level + 1)
    if (i < len(arr) - 1):
      print(f"{indentation}{relation}")


def main():
  print('---------------------')
  print_requirements(REQUIREMENTS, 1)

main()
