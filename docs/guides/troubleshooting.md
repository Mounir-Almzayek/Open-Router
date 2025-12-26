# Troubleshooting

*حل المشاكل*

## Common Issues

*المشاكل الشائعة*

### API Key Error

*خطأ مفتاح API*

**Problem**: `Authentication failed`
*المشكلة: فشل المصادقة*

**Solution**: 
*الحل:*
- Check that `OPENROUTER_API_KEY` is set in `.env`
  *تحقق من أن `OPENROUTER_API_KEY` مضبوط في `.env`*
- Verify the API key is correct
  *تحقق من أن مفتاح API صحيح*
- Make sure the key has proper permissions
  *تأكد من أن المفتاح لديه أذونات مناسبة*

### Model Not Found

*النموذج غير موجود*

**Problem**: `Model not found: model-name`
*المشكلة: النموذج غير موجود: model-name*

**Solution**:
*الحل:*
- Check model name is correct
  *تحقق من أن اسم النموذج صحيح*
- Use `GET /api/v1/models` to list available models
  *استخدم `GET /api/v1/models` لعرض النماذج المتاحة*
- Some models may require specific providers
  *بعض النماذج قد تتطلب مزودين محددين*

### File Upload Error

*خطأ رفع الملف*

**Problem**: `File size exceeds maximum`
*المشكلة: حجم الملف يتجاوز الحد الأقصى*

**Solution**:
*الحل:*
- Check file size limits in `app/config.py`
  *تحقق من حدود حجم الملف في `app/config.py`*
- Reduce file size or compress
  *قلل حجم الملف أو اضغطه*
- For videos, use `max_video_size` setting
  *للفيديو، استخدم إعداد `max_video_size`*

### Validation Error

*خطأ التحقق*

**Problem**: `Validation failed`
*المشكلة: فشل التحقق*

**Solution**:
*الحل:*
- Check error message for specific field
  *تحقق من رسالة الخطأ للحقل المحدد*
- Ensure all required fields are provided
  *تأكد من توفير جميع الحقول المطلوبة*
- Verify data types match expected types
  *تحقق من أن أنواع البيانات تطابق الأنواع المتوقعة*

## Debugging

*التشخيص*

### Enable Debug Mode

*تمكين وضع التشخيص*

Set in `.env`:
*اضبط في `.env`:*
```bash
DEBUG=True
LOG_LEVEL=DEBUG
```

### Check Logs

*تحقق من السجلات*

Logs are output to console. For production, configure proper logging.

*السجلات تُخرج إلى وحدة التحكم. للإنتاج، قم بتكوين التسجيل المناسب.*

### API Documentation

*وثائق API*

Visit `http://localhost:8000/docs` for interactive API documentation.

*زر `http://localhost:8000/docs` للوثائق التفاعلية لـ API.*

