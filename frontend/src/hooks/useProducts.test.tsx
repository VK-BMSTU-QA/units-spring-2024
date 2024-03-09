import { useProducts } from './useProducts';

describe('useProducts', () => {
  it('returns an array of products', () => {
    const products = useProducts();
    expect(Array.isArray(products)).toBe(true);
    expect(products).toHaveLength(4);
  });

  it('ensures each product to be defined', () => {
    const products = useProducts();
    products.forEach((product) => {
      expect(product.id).toBeDefined();
      expect(product.name).toBeDefined();
      expect(product.description).toBeDefined();
      expect(product.price).toBeDefined();
      expect(product.category).toBeDefined();
    });
  });

  it('ensures each product has a valid priceSymbol if provided', () => {
    const products = useProducts();
    products.forEach((product) => {
      if (product.priceSymbol) {
        expect(typeof product.priceSymbol).toBe('string');
      }
    });
  });

  it('ensures each product has a valid imgUrl if provided', () => {
    const products = useProducts();
    products.forEach((product) => {
      if (product.imgUrl) {
        expect(typeof product.imgUrl).toBe('string');
      }
    });
  });
});