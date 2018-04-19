import pytest
from inheritance import Car
from random import randint
from inheritance import Star
from inheritance import Planet

class TestsTesla:
    def test_tesla_popltn1(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(1)
        assert tesla.population == 1
    
    @pytest.mark.mark1
    @pytest.mark.mark2
    def test_tesla_popltn2(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(2)
        assert tesla.population == 2, 'Wrong population!!!111'
    
    @pytest.mark.mark1
    def test_tesla_popltn_dot5(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(.5)
        assert tesla.population == .5
    @pytest.mark.mark2
    def test_tesla_popltn_1000(self):
        tesla = Car('Roadster', 2,3,[], 6)
        tesla.send_peeps_here(1000)
        assert tesla.population == 2

        
@pytest.mark.parametrize('mass', [randint(0,1000) for x in range(5)])
@pytest.mark.parametrize('density', [randint(0,1000) for y in range(5)])
@pytest.mark.parametrize('radius', [randint(0,1000) for y in range(5)])
class TestsParametrizedCar:
    names = ['Roadster', 'Model S', 'SpaceX']  
    @pytest.mark.parametrize(('name_expected'), names)
    def test_car_name_positive(self, name_expected, mass, density, radius):
        #name_expected = 'Roadster'
        tesla = Car(name_expected, mass, density,[], radius)
        assert tesla.name == name_expected
        
    def test_car_name_whitespace_negative(self, mass, density, radius):
        name_not_alnum = 'Tesla-Roadster'
        with pytest.raises(NameError):
            Car(name_not_alnum, mass, density,[], radius)
			
@pytest.mark.parametrize('n', [randint(0,1000) for x in range(10)])
class TestsStarPopulation:
    def test_star_popltn(self, n):
        stars = Star('Star1', 2,3,[], 6)
        stars.send_peeps_here(n)
        assert stars.population == 0
			
@pytest.mark.parametrize('mass', [randint(0,9000000) for x in range(5)])
@pytest.mark.parametrize('density', [randint(0,9000000) for y in range(5)])
@pytest.mark.parametrize('radius', [randint(0,9000000) for y in range(5)])
class TestsParametrizedStar:
    names = ['LHS 2924', 'Проксіма Центавра', 'Альфа Центавра A', 'Альфа Центавра B','Сіріус А', 'Сіріус B', 'Мю Цефея', 'Зірка Барнарда', 'Зірка у Пістолеті', 'HD189733b','М31','NGC 224']  
    @pytest.mark.parametrize(('name_expected'), names)
    def test_star_name_positive(self, name_expected, mass, density, radius):
        stars = Star(name_expected, mass, density,[], radius)
        assert stars.name == name_expected
    
    names_not_alnum = ['','LHS-2924', 'Проксіма.Центавра', 'Альфа/Центавра А', 'Альфа Центавра\'B','Сіріус,А', 'Сіріус;B', 'Мю\Цефея', 'Зірка=Барнарда', 'Зірка[уПістолеті', 'HD189733{b','М_31','NG(C224']  
    @pytest.mark.parametrize(('name_not_alnum'), names_not_alnum)
    def test_star_name_negative(self, name_not_alnum, mass, density, radius):
        with pytest.raises(NameError):
            Star(name_not_alnum, mass, density,[], radius)
			
@pytest.mark.parametrize('mass', [randint(0,100000) for x in range(5)])
@pytest.mark.parametrize('density', [randint(0,100000) for y in range(5)])
@pytest.mark.parametrize('radius', [randint(0,100000) for y in range(5)])
class TestsParametrizedPlanet:
    names = ['Аврора','Альфа','Анакреонт','Арктур','Асконь','Асперта','Баронн','Бонда','Ванда','Вега','Венкорі','Вінсеторі','Ворег','Гамма Андромеда','Гелікон','Геторин','Гесперос','Гея','Гліпталь IV', 'HD1897332b','М321','NGC 2324']  
    @pytest.mark.parametrize(('name_expected'), names)
    def test_planet_name_positive(self, name_expected, mass, density, radius):
        planets = Planet(name_expected, mass, density,[], radius, 1)
        assert planets.name == name_expected
    
    names_not_alnum = ['','Авр-ора','Аль.фа','Анак\реонт','А/рктур','Аскон,ь','Ас;перта','Барон=н','Б[онда','В{анда','В_ега','Венк(орі','Вінс`еторі','Во\'рег','Гамма"Андромеда']
    @pytest.mark.parametrize(('name_not_alnum'), names_not_alnum)
    def test_planet_name_negative(self, name_not_alnum, mass, density, radius):
        with pytest.raises(NameError):
            Planet(name_not_alnum, mass, density,[], radius, 1)
