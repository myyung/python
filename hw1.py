def get_radius(prompt):
  r = int(input(prompt))
  return r

def get_circle_area():
  prompt = 0
  gr = get_radius(prompt)
  return 3.14 * gr * gr

print('넓이를 구하고자 하는 원의 반지름은?')
r = get_radius(0)
print('반지름',r,'인 원의 넓이 = 3.14 * ',r, '*', r, '=', get_circle_area())
