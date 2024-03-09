import { updateCategories } from "../updateCategories";

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(updateCategories(['Электроника', 'Одежда'], 'Одежда')).toStrictEqual(['Электроника']);
        expect(updateCategories(['Электроника', 'Одежда'], 'Для дома')).toStrictEqual(['Электроника', 'Одежда', 'Для дома']);
        expect(updateCategories(['Электроника', 'Одежда'], 'Электроника')).toStrictEqual(['Одежда']);
        expect(updateCategories(['Электроника', 'Одежда', 'Для дома'], 'Для дома')).toStrictEqual(['Электроника', 'Одежда']);
        expect(updateCategories(['Одежда'], 'Одежда')).toStrictEqual([]);
        expect(updateCategories([], 'Одежда')).toStrictEqual(['Одежда']);
    });
});
