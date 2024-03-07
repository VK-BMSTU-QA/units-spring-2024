import type { Category, Product } from '../../types';
import { useProducts } from '../../hooks';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return modified categories', () => {
        expect(updateCategories(['Электроника'], 'Для дома')).toStrictEqual([
            'Электроника',
            'Для дома',
        ]);

        expect(
            updateCategories(['Электроника', 'Для дома'], 'Для дома')
        ).toStrictEqual(['Электроника']);

        expect(updateCategories([], 'Для дома')).toStrictEqual(['Для дома']);
    });
});
