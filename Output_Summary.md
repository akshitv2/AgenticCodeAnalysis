# Java Project Analysis and Task Assignment

- **application_developer**: Focus on core business logic and data structures. Classes:
  `SpringBootEcommerceApplication.java`, `Product.java`, `Country.java`, `State.java`, `ProductCategory.java`,
  `ProductCategoryRepository.java`, `CountryRepository.java`, `StateRepository.java`, `ProductRepository.java`.
- **api_developer**: Focus on API exposure and configuration. Classes: `MyDataRestConfig.java`,
  `ProductCategoryRepository.java`, `CountryRepository.java`, `StateRepository.java`, `ProductRepository.java`.
- **journey_developer**: Focus on overall application flow and functionality. Classes:
  `SpringBootEcommerceApplication.java`, `Product.java`, `Country.java`, `State.java`, `ProductCategory.java`,
  `MyDataRestConfig.java`.
- **security_analyst**: Focus on data exposure and security implications. Classes: `MyDataRestConfig.java`.

# E-commerce Application Journey

The application initiates via `SpringBootEcommerceApplication`, defining core e-commerce entities: `Product`,
`ProductCategory`, `Country`, and `State`. `MyDataRestConfig` then customizes the exposure of these entities as REST API
endpoints through Spring Data REST. The overall journey involves bootstrapping the application, establishing the data
model, and automatically generating and configuring a RESTful API for external clients to interact with the e-commerce
data.

# Application Developer - Exposed Methods and Parameters

* **`SpringBootEcommerceApplication.java`**:
    * `main(String[] args)`: Entry point for the Spring Boot application.
* **`Product.java`**: (Entity class)
    * `getId()`: Returns `Long` product ID.
    * `getName()`: Returns `String` product name.
    * `getDescription()`: Returns `String` product description.
    * `getUnitPrice()`: Returns `BigDecimal` unit price.
    * `getImageUrl()`: Returns `String` image URL.
    * `isActive()`: Returns `boolean` active status.
    * `getUnitsInStock()`: Returns `int` units in stock.
    * `getDateCreated()`: Returns `Date` creation date.
    * `getLastUpdated()`: Returns `Date` last updated date.
    * `getCategory()`: Returns `ProductCategory` object.
    * `setId(Long id)`: Sets `Long` product ID.
    * `setName(String name)`: Sets `String` product name.
    * `setDescription(String description)`: Sets `String` product description.
    * `setUnitPrice(BigDecimal unitPrice)`: Sets `BigDecimal` unit price.
    * `setImageUrl(String imageUrl)`: Sets `String` image URL.
    * `setActive(boolean active)`: Sets `boolean` active status.
    * `setUnitsInStock(int unitsInStock)`: Sets `int` units in stock.
    * `setDateCreated(Date dateCreated)`: Sets `Date` creation date.
    * `setLastUpdated(Date lastUpdated)`: Sets `Date` last updated date.
    * `setCategory(ProductCategory category)`: Sets `ProductCategory` object.
* **`Country.java`**: (Entity class)
    * `getId()`: Returns `Integer` country ID.
    * `getCode()`: Returns `String` country code.
    * `getName()`: Returns `String` country name.
    * `getStates()`: Returns `Set<State>` associated states.
    * `setId(Integer id)`: Sets `Integer` country ID.
    * `setCode(String code)`: Sets `String` country code.
    * `setName(String name)`: Sets `String` country name.
    * `setStates(Set<State> states)`: Sets `Set<State>` associated states.
* **`State.java`**: (Entity class)
    * `getId()`: Returns `Integer` state ID.
    * `getName()`: Returns `String` state name.
    * `getCountry()`: Returns `Country` object.
    * `setId(Integer id)`: Sets `Integer` state ID.
    * `setName(String name)`: Sets `String` state name.
    * `setCountry(Country country)`: Sets `Country` object.
* **`ProductCategory.java`**: (Entity class)
    * `getId()`: Returns `Long` category ID.
    * `getCategoryName()`: Returns `String` category name.
    * `getProducts()`: Returns `Set<Product>` associated products.
    * `setId(Long id)`: Sets `Long` category ID.
    * `setCategoryName(String categoryName)`: Sets `String` category name.
    * `setProducts(Set<Product> products)`: Sets `Set<Product>` associated products.
* **`ProductCategoryRepository.java`**: (Spring Data JPA Repository - extends `JpaRepository<ProductCategory, Long>`)
    * Inherits standard CRUD methods: `findAll()`, `findById(Long id)`, `save(ProductCategory entity)`,
      `delete(ProductCategory entity)`, etc.
* **`CountryRepository.java`**: (Spring Data JPA Repository - extends `JpaRepository<Country, Integer>`)
    * Inherits standard CRUD methods: `findAll()`, `findById(Integer id)`, `save(Country entity)`,
      `delete(Country entity)`, etc.
* **`StateRepository.java`**: (Spring Data JPA Repository - extends `JpaRepository<State, Integer>`)
    * Inherits standard CRUD methods: `findAll()`, `findById(Integer id)`, `save(State entity)`, `delete(State entity)`,
      etc.
* **`ProductRepository.java`**: (Spring Data JPA Repository - extends `JpaRepository<Product, Long>`)
    * Inherits standard CRUD methods: `findAll()`, `findById(Long id)`, `save(Product entity)`,
      `delete(Product entity)`, etc.
    * `findByCategoryId(@Param("id") Long id, Pageable pageable)`: Returns `Page<Product>` filtered by category ID.
    * `findByNameContaining(@Param("name") String name, Pageable pageable)`: Returns `Page<Product>` filtered by product
      name containing a given string.
* `GET /api/products`, `GET /api/products/{id}`: Products CRUD
* `GET /api/product-categories`, `GET /api/product-categories/{id}`: Product Categories CRUD
* `GET /api/countries`, `GET /api/countries/{id}`: Countries CRUD
* `GET /api/states`, `GET /api/states/{id}`: States CRUD
* `GET /api/products/search/findByCategoryId?id={id}`: Products by Category
* `GET /api/products/search/findByNameContaining?name={name}`: Products by Name (partial match)

# Security Report

| Dependency                                                                                | CVE                                 |
|-------------------------------------------------------------------------------------------|-------------------------------------|
| org.springframework.boot:spring-boot-starter-parent:2.7.5 (and implied Spring Boot 2.7.5) | CVE-2023-34055                      |
| org.springframework.boot:spring-boot-starter-parent:2.7.5 (and implied Spring Boot 2.7.5) | CVE-2025-9784 (Future/Placeholder)  |
| org.springframework.boot:spring-boot-starter-parent:2.7.5 (and implied Spring Boot 2.7.5) | CVE-2025-52999 (Future/Placeholder) |
| mysql:mysql-connector-java:8.0.30                                                         | CVE-2023-22102                      |
| mysql:mysql-connector-java:8.0.30                                                         | CVE-2023-21971                      |
| mysql:mysql-connector-java:8.0.30                                                         | CVE-2024-7254 (Future/Placeholder)  |
| mysql:mysql-connector-java:8.0.30                                                         | CVE-2022-3510                       |
| mysql:mysql-connector-java:8.0.30                                                         | CVE-2022-3509                       |
| mysql:mysql-connector-java:8.0.30                                                         | CVE-2022-3171                       |
| org.projectlombok:lombok:1.18.24                                                          | No direct CVEs found                |
