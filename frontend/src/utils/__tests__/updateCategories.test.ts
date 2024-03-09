import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    it('should return category', () => {
        expect(updateCategories([], 'Электроника')). toStrictEqual(['Электроника']);
    });

    it('should return categories', () => {
        expect(updateCategories(['Электроника'], 'Одежда')). toStrictEqual(['Электроника', 'Одежда']);
    });

    it('should remove category', () => {
        expect(updateCategories(['Электроника'], 'Электроника')). toStrictEqual([]);
    });
});