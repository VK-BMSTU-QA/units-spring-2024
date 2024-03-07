import { getPrice } from '../getPrice';
import { applyCategories } from '../applyCategories';
import { updateCategories } from '../updateCategories';
import { useProducts } from '../../hooks/useProducts';

describe('test get price function', () => {
    it('should return value with price symbol', () => {
        expect(getPrice(100, '₽')).toBe('100 ₽');
        expect(getPrice(325, '$')).toBe('325 $');
    });
});

describe('test apply categories function', () => {
    it('should return products with given category', () => {
        expect(applyCategories([useProducts()[0]], [])).toStrictEqual([
            useProducts()[0],
        ]);
        expect(
            applyCategories(
                [useProducts()[0], useProducts()[1]],
                ['Электроника']
            )
        ).toStrictEqual([useProducts()[0]]);
    });
});

describe('test update categories', () => {
    it('should return updated categories', () => {
        expect(
            updateCategories(['Для дома', 'Одежда'], 'Электроника')
        ).toStrictEqual(['Для дома', 'Одежда', 'Электроника']);
        expect(
            updateCategories(['Для дома', 'Одежда'], 'Одежда')
        ).toStrictEqual(['Для дома']);
    });
});
