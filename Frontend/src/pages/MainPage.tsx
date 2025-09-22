import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import type { Department, Product } from './mockData';
import { departmentsData } from './mockData';

export default function MainPage() {
  const [currentSectionId, setCurrentSectionId] = useState<string>('all');
  const [products, setProducts] = useState<Product[]>([]);
  const [filters, setFilters] = useState({
    Published: true,
    'For Revision': false,
    Draft: false,
  });

  // This effect simulates fetching data based on the selected section and filters
  useEffect(() => {
    const selectedSection = departmentsData.find(dept => dept.id === currentSectionId);
    if (selectedSection) {
      const filteredProducts = selectedSection.products.filter(product => {
        if (filters[product.status as keyof typeof filters]) {
          return true;
        }
        return false;
      });
      setProducts(filteredProducts);
    }
  }, [currentSectionId, filters]);

  const handleFilterChange = (filterName: keyof typeof filters) => {
    setFilters(prev => ({
      ...prev,
      [filterName]: !prev[filterName],
    }));
  };

  const selectedSectionName = departmentsData.find(d => d.id === currentSectionId)?.name || 'All Products';
  const totalProducts = departmentsData[0].products.length;
  const pendingRevisions = departmentsData[0].products.filter(p => p.status === 'For Revision').length;
  const published = departmentsData[0].products.filter(p => p.status === 'Published').length;

  return (
    <div className="h-screen flex flex-col bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm p-4 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <svg className="w-8 h-8 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM6 11a1 1 0 100 2h8a1 1 0 100-2H6z" clipRule="evenodd" fillRule="evenodd"></path>
          </svg>
          <h1 className="text-2xl font-semibold text-gray-800">PIM Dashboard</h1>
        </div>
      </header>

      {/* Main Content Area */}
      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <aside className="w-64 bg-white p-4 overflow-y-auto border-r border-gray-200">
          <h2 className="text-lg font-semibold text-gray-700 mb-4">Sections</h2>
          <nav className="space-y-2">
            {departmentsData.map(dept => (
              <button
                key={dept.id}
                onClick={() => setCurrentSectionId(dept.id)}
                className={`flex items-center w-full px-3 py-2 rounded-lg text-left transition-colors duration-200 focus:outline-none ${currentSectionId === dept.id ? 'bg-gray-200' : 'hover:bg-gray-100'}`}
              >
                <svg className="w-5 h-5 mr-2 text-gray-500" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                </svg>
                <span className="text-sm font-medium text-gray-700">{dept.name}</span>
              </button>
            ))}
          </nav>
          <div className="mt-8 border-t border-gray-200 pt-4">
            <h2 className="text-lg font-semibold text-gray-700 mb-4">Filters</h2>
            <div className="space-y-2">
              {Object.keys(filters).map(key => (
                <label key={key} className="flex items-center space-x-2 text-sm text-gray-600">
                  <input
                    type="checkbox"
                    checked={filters[key as keyof typeof filters]}
                    onChange={() => handleFilterChange(key as keyof typeof filters)}
                    className="rounded text-blue-600 focus:ring-blue-500"
                  />
                  <span>{key}</span>
                </label>
              ))}
            </div>
          </div>
        </aside>

        {/* Main Dashboard View */}
        <main className="flex-1 p-6 overflow-y-auto">
          {/* Summary Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200 text-center">
              <p className="text-lg text-gray-500">Total Products</p>
              <h3 className="text-4xl font-bold text-gray-800 mt-2">{totalProducts}</h3>
            </div>
            <div className="bg-white rounded-xl p-6 shadow-md border border-yellow-300 bg-yellow-50 text-center">
              <p className="text-lg text-gray-500">Pending Revisions</p>
              <h3 className="text-4xl font-bold text-yellow-600 mt-2">{pendingRevisions}</h3>
            </div>
            <div className="bg-white rounded-xl p-6 shadow-md border border-green-300 bg-green-50 text-center">
              <p className="text-lg text-gray-500">Published</p>
              <h3 className="text-4xl font-bold text-green-600 mt-2">{published}</h3>
            </div>
          </div>

          <div className="flex items-center justify-between mb-6">
            <h2 id="current-department" className="text-3xl font-bold text-gray-900">{selectedSectionName}</h2>
            <div className="flex items-center space-x-4">
              <input type="text" placeholder="Search for products..." className="px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-colors duration-200 w-64" />
              <button className="bg-blue-600 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-colors duration-200">
                <span className="font-medium">+ Add Product</span>
              </button>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {products.map((product, index) => {
              const statusColor = product.status === 'Published' ? 'text-green-500' :
                product.status === 'For Revision' ? 'text-yellow-500' : 'text-gray-500';

              return (
                <div key={index} className="bg-white rounded-xl p-4 shadow-md border border-gray-200 flex flex-col space-y-2">
                  <div className="h-40 bg-gray-100 rounded-lg flex items-center justify-center text-gray-400 font-semibold text-sm">
                    {/* Placeholder for an image */}
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-semibold text-gray-800">{product.name}</h3>
                    <p className="text-sm text-gray-500">{product.brand}</p>
                    <p className={`text-sm font-medium mt-1 ${statusColor}`}>{product.status}</p>
                    {product.note && (
                      <p className="text-xs text-yellow-600 bg-yellow-100 p-2 rounded-md mt-2">{product.note}</p>
                    )}
                  </div>
                  <div className="flex items-center justify-between">
                    <button className="text-gray-400 hover:text-red-500">
                      <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm6 0a1 1 0 11-2 0v6a1 1 0 112 0V8z" clipRule="evenodd"></path></svg>
                    </button>
                    <Link to={`/product/${index}`} className="bg-blue-100 text-blue-600 px-3 py-1 text-sm rounded-full font-medium hover:bg-blue-200 transition-colors duration-200">
                      View Product
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        </main>
      </div>
    </div>
  );
}