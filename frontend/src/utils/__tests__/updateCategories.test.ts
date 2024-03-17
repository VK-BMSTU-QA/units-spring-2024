import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update Categories function', () => {
    it('should add category to array', () => {
        const category: Category[] = ['Для дома', 'Одежда'];
        expect(updateCategories(category, 'Электроника')).toStrictEqual([
            'Для дома',
            'Одежда',
            'Электроника',
        ]);
        expect(updateCategories([], 'Одежда')).toStrictEqual(['Одежда']);
    });

    it('should remove category from array', () => {
        const category: Category[] = ['Для дома', 'Одежда'];
        expect(updateCategories(category, 'Одежда')).toStrictEqual([
            'Для дома',
        ]);
        expect(updateCategories(['Одежда'], 'Одежда')).toStrictEqual([]);
    });
});
