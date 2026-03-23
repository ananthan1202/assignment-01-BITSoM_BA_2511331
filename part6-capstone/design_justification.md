Storage Systems

The proposed architecture uses multiple storage systems to support the different operational and analytical requirements of the hospital network. A relational transactional database such as PostgreSQL is used as the primary OLTP system. This database stores structured hospital records including patient demographics, treatment history, doctor visits, prescriptions, and billing information. Transactional databases are designed to support high-frequency updates and ensure data consistency, which is essential in healthcare systems where accuracy and reliability are critical.

For handling large volumes of raw and semi-structured data, a data lake such as Amazon S3 or Azure Data Lake Storage is used. The data lake stores raw ICU monitoring data streams, device logs, clinical notes, and other large datasets that may not follow a strict schema. This environment enables the hospital to collect and retain large amounts of data at relatively low cost while maintaining flexibility for future analytics and machine learning applications.

For analytical workloads, a cloud data warehouse such as Snowflake or Google BigQuery is used. Data from operational systems and the data lake is periodically transformed and loaded into the warehouse using ETL pipelines. The warehouse supports complex analytical queries and reporting tasks such as hospital performance metrics, departmental cost analysis, and monthly management reports. By separating operational and analytical workloads, the architecture ensures that reporting and analytics do not interfere with day-to-day hospital operations.

OLTP vs OLAP Boundary

The architecture clearly separates transactional processing (OLTP) from analytical processing (OLAP). The OLTP layer is responsible for real-time hospital operations such as patient admissions, updating medical records, scheduling appointments, and processing billing transactions. These activities require fast, reliable write operations and strong consistency, which are handled by the transactional database system.

The OLAP boundary begins when operational data is extracted from the transactional systems and transferred to analytical storage layers. Data pipelines move relevant information into the data lake and the data warehouse for large-scale analysis. The data warehouse is optimized for read-intensive analytical queries and supports reporting dashboards used by hospital administrators and management teams. This separation allows operational systems to remain responsive while enabling complex analytical workloads on historical data.

Trade-offs

One significant trade-off in this architecture is the increased complexity introduced by maintaining multiple data systems. The combination of transactional databases, data lakes, and data warehouses requires careful data integration and management. Data pipelines must reliably transfer information between systems, and maintaining data consistency across platforms can be challenging.

However, this trade-off is justified by the scalability and flexibility gained from this design. The architecture allows the hospital to efficiently handle both real-time operational data and large-scale analytical workloads. To mitigate the complexity, the system can use automated orchestration tools and managed cloud services to handle data movement and infrastructure management. Technologies such as automated ETL pipelines and cloud monitoring tools can ensure reliable data flow while reducing operational overhead.

Overall, this architecture provides a scalable and flexible foundation for supporting AI-driven healthcare applications, real-time monitoring, and advanced analytics, enabling the hospital network to improve patient outcomes and operational efficiency.