export type ProductStatus = 'Published' | 'For Revision' | 'Draft';

export interface Product {
  name: string;
  brand: string;
  status: ProductStatus;
  note: string | null;
}

export interface Department {
  id: string;
  name: string;
  products: Product[];
}

export const departmentsData: Department[] = [
  {
    id: 'all',
    name: 'All Products',
    products: [
      { name: 'FP1 Flat Tarpaulin 207.5 x 114 cm', brand: 'Tarpofix', status: 'Published', note: null },
      { name: 'HD Bungee Cords', brand: 'Planenfux', status: 'For Revision', note: null },
      { name: 'Pro-Grade Tie-Down Straps', brand: 'Planenfux', status: 'Draft', note: null },
      { name: 'Canvas Work Trousers', brand: 'Hemfleiss', status: 'Published', note: null },
      { name: 'Product E', brand: 'Tarpofix', status: 'Published', note: null },
      { name: 'Product F', brand: 'Hemfleiss', status: 'Published', note: 'Note: Customer requested a different color.' },
      { name: 'Custom Tool Kit', brand: 'Mattenheld', status: 'For Revision', note: 'Needs new photos.' },
      { name: 'Winter Gloves', brand: 'Hemfleiss', status: 'Published', note: null }
    ]
  },
  {
    id: 'tarpofix',
    name: 'Tarpofix',
    products: [
      { name: 'FP1 Flat Tarpaulin 207.5 x 114 cm', brand: 'Tarpofix', status: 'Published', note: null },
      { name: 'Product E', brand: 'Tarpofix', status: 'Published', note: null }
    ]
  },
  {
    id: 'Planenfux',
    name: 'Planenfux',
    products: [
      { name: 'HD Bungee Cords', brand: 'Planenfux', status: 'For Revision', note: null },
      { name: 'Pro-Grade Tie-Down Straps', brand: 'Planenfux', status: 'Draft', note: null }
    ]
  },
  {
    id: 'Hemfleiss',
    name: 'Hemfleiss',
    products: [
      { name: 'Canvas Work Trousers', brand: 'Hemfleiss', status: 'Published', note: null },
      { name: 'Product F', brand: 'Hemfleiss', status: 'Published', note: 'Note: Customer requested a different color.' },
      { name: 'Winter Gloves', brand: 'Hemfleiss', status: 'Published', note: null }
    ]
  },
  {
    id: 'Mattenheld',
    name: 'Mattenheld',
    products: [
      { name: 'Custom Tool Kit', brand: 'Mattenheld', status: 'For Revision', note: 'Needs new photos.' }
    ]
  }
];