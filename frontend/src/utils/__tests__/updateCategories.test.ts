import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return value needs categories', () => {
        expect(updateCategories([], 'Для дома')).toStrictEqual(['Для дома']);
        expect(updateCategories(['Для дома'], 'Для дома')).toStrictEqual([]);
        expect(updateCategories(['Для дома', 'Электроника'], 'Одежда')).toStrictEqual(['Для дома', 'Электроника', 'Одежда'])
    });
});
