# Zero Data Retention (ZDR)

## Feature Overview

Zero Data Retention (ZDR) ensures that providers don't store your data after processing requests. When enabled, providers are required to delete your data immediately after processing, preventing data retention, training use, or any other data storage. This feature provides strong privacy guarantees for sensitive applications.

*عدم الاحتفاظ بالبيانات (ZDR) يضمن أن المزودين لا يخزنون بياناتك بعد معالجة الطلبات. عند التمكين، يُطلب من المزودين حذف بياناتك فوراً بعد المعالجة، مما يمنع الاحتفاظ بالبيانات أو استخدام التدريب أو أي تخزين بيانات آخر. هذه الميزة توفر ضمانات خصوصية قوية للتطبيقات الحساسة.*

## Feature Importance

ZDR is essential for applications handling sensitive data—medical records, financial information, personal data, or confidential business information. Without ZDR, providers may store your data for training, analysis, or other purposes, creating privacy and compliance risks. ZDR ensures data privacy and helps meet regulatory requirements like GDPR and HIPAA.

*ZDR ضروري للتطبيقات التي تتعامل مع البيانات الحساسة—السجلات الطبية أو المعلومات المالية أو البيانات الشخصية أو معلومات الأعمال السرية. بدون ZDR، قد يخزن المزودون بياناتك للتدريب أو التحليل أو أغراض أخرى، مما يخلق مخاطر الخصوصية والامتثال. ZDR يضمن خصوصية البيانات ويساعد في تلبية المتطلبات التنظيمية مثل GDPR وHIPAA.*

## Key Benefits

### Privacy Protection
Prevents providers from storing your data, ensuring sensitive information isn't retained or used for purposes beyond your immediate request processing.

*يمنع المزودين من تخزين بياناتك، مما يضمن عدم الاحتفاظ بالمعلومات الحساسة أو استخدامها لأغراض تتجاوز معالجة طلبك الفوري.*

### Compliance Support
Helps meet regulatory requirements like GDPR, HIPAA, and other privacy regulations that require data minimization and restricted retention.

*يساعد في تلبية المتطلبات التنظيمية مثل GDPR وHIPAA واللوائح الأخرى التي تتطلب تقليل البيانات والاحتفاظ المقيد.*

### Data Security
Reduces data exposure by ensuring data isn't stored in provider systems longer than necessary. This minimizes the risk of data breaches or unauthorized access.

*يقلل تعرض البيانات عن طريق ضمان عدم تخزين البيانات في أنظمة المزودين لفترة أطول من اللازم. هذا يقلل مخاطر انتهاكات البيانات أو الوصول غير المصرح به.*

## Enable ZDR

*تمكين ZDR*

```python
from app.builders import ChatRequestBuilder

request = (ChatRequestBuilder()
    .with_model("openai/gpt-4o")
    .with_text("Sensitive information")
    .with_zdr(enabled=True)
    .build())
```

## What ZDR Does

- Prevents providers from storing your requests
  *يمنع المزودين من تخزين طلباتك*
- Ensures data is not used for training
  *يضمن عدم استخدام البيانات للتدريب*
- Provides privacy guarantees
  *يوفر ضمانات الخصوصية*

## When to Use

- **Sensitive Data**: Personal information, medical data, financial data
  *البيانات الحساسة: المعلومات الشخصية، البيانات الطبية، البيانات المالية*
- **Compliance**: GDPR, HIPAA, or other privacy regulations
  *الامتثال: GDPR أو HIPAA أو لوائح الخصوصية الأخرى*
- **Confidentiality**: Internal business information
  *السرية: معلومات الأعمال الداخلية*

## Limitations

- Not all providers support ZDR
  *ليس جميع المزودين يدعمون ZDR*
- May have higher costs
  *قد يكون لديه تكاليف أعلى*
- May have performance impact
  *قد يكون لديه تأثير على الأداء*

## Example

```python
request = (ChatRequestBuilder()
    .with_model("anthropic/claude-sonnet-4")
    .with_text("Patient medical record analysis")
    .with_zdr(enabled=True)
    .with_data_collection(DataCollection.DENY)
    .build())
```

