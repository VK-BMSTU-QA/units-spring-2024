import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update Categories function', () => {
    it('should return array with categories', () => {
        const category: Category[] = ['Для дома', 'Одежда'];
        expect(updateCategories(category, 'Электроника')).toStrictEqual([
            'Для дома',
            'Одежда',
            'Электроника',
        ]);
        expect(updateCategories(category, 'Одежда')).toStrictEqual([
            'Для дома',
        ]);
        expect(updateCategories([], 'Одежда')).toStrictEqual(['Одежда']);
        expect(updateCategories(['Одежда'], 'Одежда')).toStrictEqual([]);
    });
});
