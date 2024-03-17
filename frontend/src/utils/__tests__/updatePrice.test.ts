import { updateCategories } from "../updateCategories";

describe('test get price function', () => {
    it('should add values which are not in categories', () => {
        expect(updateCategories(['Электроника', 'Одежда'], 'Для дома')).toStrictEqual(['Электроника', 'Одежда', 'Для дома']);
        expect(updateCategories([], 'Одежда')).toStrictEqual(['Одежда']);
    });

    it('should delete values which are in categories', () => {
        expect(updateCategories(['Электроника', 'Одежда'], 'Одежда')).toStrictEqual(['Электроника']);
        expect(updateCategories(['Электроника', 'Одежда'], 'Электроника')).toStrictEqual(['Одежда']);
        expect(updateCategories(['Электроника', 'Одежда', 'Для дома'], 'Для дома')).toStrictEqual(['Электроника', 'Одежда']);
        expect(updateCategories(['Одежда'], 'Одежда')).toStrictEqual([]);
    });
});
