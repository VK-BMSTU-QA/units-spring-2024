import { applyCategories } from '../applyCategories';
import { useProducts } from '../../hooks/useProducts';

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
