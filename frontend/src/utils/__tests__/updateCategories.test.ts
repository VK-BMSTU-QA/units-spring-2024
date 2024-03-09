import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test updateCategories', () => {
    it('should toggle category in categories', () => {
        expect(updateCategories(['Для дома', 'Одежда'] as Category[], 'Для дома')).toEqual([
            'Одежда',
        ]);

        expect(updateCategories(['Для дома', 'Одежда'] as Category[], 'Электроника')).toEqual(
            ['Для дома', 'Одежда', 'Электроника']
        );

        expect(updateCategories([] as Category[], 'Электроника')).toEqual(['Электроника']);
    });
});