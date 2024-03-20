import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return all categories added to an empty list', () => {
        expect(updateCategories([], 'Для дома')).toStrictEqual(['Для дома']);
    });

    it('should return a list of categories by deleting the necessary ones', () => {
        expect(updateCategories(['Для дома'], 'Для дома')).toStrictEqual([]);
    });
    
    it('should return a list of categories by adding new categories', () => {
        expect(updateCategories(['Для дома', 'Электроника'], 'Одежда')).toStrictEqual(['Для дома', 'Электроника', 'Одежда'])
    });
});
