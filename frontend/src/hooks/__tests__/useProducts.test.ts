import { useProducts } from '../useProducts';

describe('test UseProduct hook', () => {
    it('UseProduct return array and len >= 0', () => {
        const products = useProducts();
        expect(Array.isArray(products));
        expect(products.length).toBeGreaterThan(0);
    });

    it('test product parameters in hooks return', () => {
        const products = useProducts();
        products.forEach((product) => {
            expect(product).toHaveProperty('id');
            expect(product).toHaveProperty('name');
            expect(product).toHaveProperty('description');
            expect(product).toHaveProperty('price');
            expect(product).toHaveProperty('category');

            if (product.imgUrl) {
                expect(product).toHaveProperty('imgUrl');
            }

            if (product.priceSymbol) {
                expect(product).toHaveProperty('priceSymbol');
            }
        });
    });
});

