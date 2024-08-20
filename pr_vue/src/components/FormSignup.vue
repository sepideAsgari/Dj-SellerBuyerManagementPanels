<template>
  <div class="registration-container">
    <h1 class="title">ثبت‌نام فروشنده</h1>
    <div class="field">
      <label class="label">نام کامل خود را وارد کنید</label>
      <div class="control">
        <input class="input this-is-rtl" type="text" v-model="fullname" placeholder="نام کامل">
      </div>
    </div>
    <div class="field">
      <label class="label">استان خود را انتخاب کنید</label>
      <div class="control">
        <div class="select">
          <select class="this-is-rtl" v-model="selectedProvince" @change="updateCities">
            <option class="this-is-rtl" value="" disabled>انتخاب استان</option>
            <option class="this-is-rtl" v-for="province in provinces" :key="province.name" :value="province.name">{{ province.name }}
            </option>
          </select>
        </div>
      </div>
    </div>
    <div class="field" v-if="selectedProvince">
      <label class="label">شهر خود را انتخاب کنید</label>
      <div class="control">
        <div class="select">
          <select class="this-is-rtl" v-model="selectedCity">
            <option class="this-is-rtl" value="" disabled>انتخاب شهر</option>
            <option class="this-is-rtl" v-for="city in cities" :key="city">{{ city }}</option>
          </select>
        </div>
      </div>
    </div>
    <div class="field">
      <label class="label">لطفا ایمیل خود را وارد کنید</label>
      <div class="control">
        <input class="input" type="email" v-model="email" placeholder="company@gmail.com">
      </div>
    </div>
    <div class="field">
      <label class="label">لطفا رمز عبور خود را وارد کنید</label>
      <div class="control">
        <input class="input" type="password" v-model="password" placeholder="* * * * * * * *">
      </div>
    </div>
    <div class="field">
      <label class="label">لطفا رمز عبور خود را مجددا وارد کنید</label>
      <div class="control">
        <input class="input" type="password" v-model="password2" placeholder="* * * * * * * *">
      </div>
    </div>
    <div class="field">
      <div class="control">
        <button class="button is-primary" @click="submitForm">ثبت‌نام</button>
      </div>
    </div>
    <hr>
    <div class="field">
      <div class="label">
        یا <router-link class="has-text-link" to="/vendor/log-in">جهت ورود</router-link> کلیک کنید!
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import NoFooterMixin from '@/components/mixins/NoFooterMixin.js'

export default {
  name: 'FormSignup',
  mixins: [NoFooterMixin],
  data() {
    return {
      fullname: '',
      email: '',
      password: '',
      password2: '',
      user_type: 'vendor',
      selectedProvince: '',
      selectedCity: '',
      provinces: [
        {
          name: 'آذربایجان شرقی',
          cities: ['تبریز', 'مراغه', 'مرند', 'میانه', 'اهر', 'بناب', 'سراب', 'شبستر', 'بستان‌آباد', 'هریس', 'هشترود', 'کلیبر', 'ورزقان', 'چاراویماق']
        },
        {
          name: 'آذربایجان غربی',
          cities: ['ارومیه', 'خوی', 'میاندوآب', 'مهاباد', 'بوکان', 'سلماس', 'پیرانشهر', 'سردشت', 'نقده', 'اشنویه', 'شاهین‌دژ', 'چالدران', 'شوط', 'ماکو', 'پلدشت']
        },
        {
          name: 'اردبیل',
          cities: ['اردبیل', 'پارس‌آباد', 'مشگین‌شهر', 'خلخال', 'گرمی', 'بیله‌سوار', 'نیر', 'نمین', 'کوثر']
        },
        {
          name: 'اصفهان',
          cities: ['اصفهان', 'کاشان', 'خمینی‌شهر', 'نجف‌آباد', 'فلاورجان', 'لنجان', 'مبارکه', 'شهرضا', 'سمیرم', 'نطنز', 'اردستان', 'برخوار', 'فریدن', 'چادگان', 'خوانسار', 'تیران و کرون']
        },
        {
          name: 'البرز',
          cities: ['کرج', 'فردیس', 'ساوجبلاغ', 'نظرآباد', 'اشتهارد', 'طالقان']
        },
        {
          name: 'ایلام',
          cities: ['ایلام', 'دهلران', 'مهران', 'آبدانان', 'ایوان', 'دره‌شهر', 'چرداول', 'ملکشاهی', 'بدره']
        },
        {
          name: 'بوشهر',
          cities: ['بوشهر', 'برازجان', 'جم', 'کنگان', 'گناوه', 'دیلم', 'دشتی', 'دیر', 'تنگستان', 'دشتستان']
        },
        {
          name: 'تهران',
          cities: ['تهران', 'ری', 'شمیرانات', 'ورامین', 'شهریار', 'اسلامشهر', 'بهارستان', 'رباط‌کریم', 'قدس', 'پاکدشت', 'ملارد', 'دماوند', 'فیروزکوه']
        },
        {
          name: 'چهارمحال و بختیاری',
          cities: ['شهرکرد', 'بروجن', 'فارسان', 'لردگان', 'اردل', 'کوهرنگ', 'کیار', 'سامان', 'بن']
        },
        {
          name: 'خراسان جنوبی',
          cities: ['بیرجند', 'قاین', 'فردوس', 'نهبندان', 'سربیشه', 'بشرویه', 'درمیان', 'سرایان', 'خوسف', 'زیرکوه']
        },
        {
          name: 'خراسان رضوی',
          cities: ['مشهد', 'نیشابور', 'سبزوار', 'تربت حیدریه', 'قوچان', 'گناباد', 'کاشمر', 'تربت‌جام', 'خواف', 'چناران', 'درگز', 'سرخس', 'فریمان', 'خلیل‌آباد', 'بجستان', 'طرقبه شاندیز', 'رشتخوار']
        },
        {
          name: 'خراسان شمالی',
          cities: ['بجنورد', 'اسفراین', 'شیروان', 'فاروج', 'مانه و سملقان', 'جاجرم', 'گرمه', 'راز و جرگلان']
        },
        {
          name: 'خوزستان',
          cities: ['اهواز', 'آبادان', 'خرمشهر', 'دزفول', 'اندیمشک', 'شوشتر', 'ماهشهر', 'شادگان', 'مسجدسلیمان', 'ایذه', 'باغ‌ملک', 'بهبهان', 'رامهرمز', 'امیدیه', 'هندیجان', 'رامشیر', 'حمیدیه']
        },
        {
          name: 'زنجان',
          cities: ['زنجان', 'ابهر', 'خرمدره', 'قیدار', 'سلطانیه', 'طارم', 'ماهنشان', 'ایجرود']
        },
        {
          name: 'سمنان',
          cities: ['سمنان', 'شاهرود', 'دامغان', 'گرمسار', 'مهدیشهر', 'سرخه', 'آرادان', 'میامی']
        },
        {
          name: 'سیستان و بلوچستان',
          cities: ['زاهدان', 'چابهار', 'ایرانشهر', 'خاش', 'سراوان', 'نیک‌شهر', 'سرباز', 'کنارک', 'قصرقند', 'زهک', 'هیرمند', 'دلگان', 'مهرستان', 'بمپور', 'فنوج', 'میرجاوه', 'نیمروز']
        },
        {
          name: 'فارس',
          cities: ['شیراز', 'مرودشت', 'کازرون', 'جهرم', 'لار', 'فسا', 'داراب', 'ممسنی', 'آباده', 'نی‌ریز', 'اقلید', 'سپیدان', 'خرامه', 'خنج', 'کوار', 'زرین‌دشت', 'بوانات', 'رستم', 'قیر و کارزین']
        },
        {
          name: 'قزوین',
          cities: ['قزوین', 'البرز', 'آبیک', 'بوئین‌زهرا', 'تاکستان', 'آوج']
        },
        {
          name: 'قم',
          cities: ['قم']
        },
        {
          name: 'کردستان',
          cities: ['سنندج', 'سقز', 'مریوان', 'بانه', 'بیجار', 'قروه', 'دیواندره', 'کامیاران', 'دهگلان']
        },
        {
          name: 'کرمان',
          cities: ['کرمان', 'رفسنجان', 'جیرفت', 'سیرجان', 'بم', 'زرند', 'بافت', 'شهربابک', 'بردسیر', 'کوهبنان', 'انار', 'ریگان', 'فهرج', 'رودبار جنوب', 'عنبرآباد', 'ارزوییه']
        },
        {
          name: 'کرمانشاه',
          cities: ['کرمانشاه', 'اسلام‌آباد غرب', 'هرسین', 'سنقر', 'قصر شیرین', 'کنگاور', 'جوانرود', 'سرپل ذهاب', 'صحنه', 'روانسر', 'پاوه', 'گیلانغرب', 'دالاهو', 'ثلاث باباجانی']
        },
        {
          name: 'کهگیلویه و بویراحمد',
          cities: ['یاسوج', 'دهدشت', 'گچساران', 'باشت', 'لنده', 'بهمئی', 'چرام', 'دنا']
        },
        {
          name: 'گلستان',
          cities: ['گرگان', 'گنبد کاووس', 'علی‌آباد کتول', 'آق‌قلا', 'مینودشت', 'بندر ترکمن', 'کلاله', 'کردکوی', 'آزادشهر', 'گمیشان', 'رامیان', 'مراوه‌تپه', 'بندر گز']
        },
        {
          name: 'گیلان',
          cities: ['رشت', 'بندر انزلی', 'لاهیجان', 'آستارا', 'رودسر', 'تالش', 'صومعه‌سرا', 'رودبار', 'فومن', 'لنگرود', 'ماسال', 'آستانه اشرفیه', 'شفت', 'رضوانشهر', 'املش']
        },
        {
          name: 'لرستان',
          cities: ['خرم‌آباد', 'بروجرد', 'دورود', 'کوهدشت', 'الیگودرز', 'ازنا', 'پلدختر', 'دلفان', 'سلسله']
        },
        {
          name: 'مازندران',
          cities: ['ساری', 'بابل', 'آمل', 'قائم‌شهر', 'نوشهر', 'چالوس', 'رامسر', 'بهشهر', 'تنکابن', 'بابلسر', 'جویبار', 'نور', 'محمودآباد', 'فریدونکنار', 'نکا', 'کلاردشت', 'سوادکوه']
        },
        {
          name: 'مرکزی',
          cities: ['اراک', 'ساوه', 'خمین', 'محلات', 'شازند', 'تفرش', 'دلیجان', 'کمیجان', 'خنداب', 'آشتیان']
        },
        {
          name: 'هرمزگان',
          cities: ['بندرعباس', 'میناب', 'بندر لنگه', 'قشم', 'بستک', 'حاجی‌آباد', 'جاسک', 'خمیر', 'رودان', 'پارسیان', 'سیریک', 'بشاگرد']
        },
        {
          name: 'همدان',
          cities: ['همدان', 'ملایر', 'نهاوند', 'کبودرآهنگ', 'تویسرکان', 'رزن', 'بهار', 'اسدآباد', 'فامنین']
        },
        {
          name: 'یزد',
          cities: ['یزد', 'میبد', 'اردکان', 'ابرکوه', 'بافق', 'مهریز', 'خاتم', 'تفت', 'اشکذر']
        }
      ],
      cities: [],
    };
  },
  mounted() {
    this.$store.commit('hideFooter')
  },
  beforeUnmount() {
    this.$store.commit('showFooter')
  },
  methods: {
    updateCities() {
      const province = this.provinces.find(p => p.name === this.selectedProvince);
      this.cities = province ? province.cities : [];
      this.selectedCity = '';
    },
    submitForm() {
      this.errors = [];

      if (this.fullname === '') {
        toast({
          message: 'اطلاعات هویتی خود را وارد کنید.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        });
      }

      if (this.email === '') {
        toast({
          message: 'ایمیل نباید خالی باشد.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        });
      }

      if (this.password === '') {
        toast({
          message: 'رمز عبور نباید خالی باشد.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        });
      }

      if (this.password !== this.password2) {
        toast({
          message: 'رمز عبور همخوانی ندارد.',
          type: 'is-warning',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        });
        return;
      }

      if (!this.errors.length) {
        const formData = {
          full_name: this.fullname,
          username: this.email,
          email: this.email,
          password: this.password,
          user_type: this.user_type,
          province: this.selectedProvince,
          city: this.selectedCity,
        };
        console.log(formData);

        axios
          .post("/api/v1/vendors/", formData)
          .then(response => {
            toast({
              message: 'حساب کاربری ایجاد شد.',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'bottom-right',
            });

            this.$router.push('/vendor/log-in');
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                if (property === 'username') {
                  toast({
                    message: `ایمیل موجود می باشد.`,
                    type: 'is-warning',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 3000,
                    position: 'bottom-right',
                  });
                } else {
                  this.errors.push('رمز عبور همخوانی ندارد.');
                }
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push('Something went wrong. Please try again');
              console.log(JSON.stringify(error));
            }
          });
      }
    }
  }
};
</script>

<style lang="scss">
.subtitle {
  direction: rtl !important;
}

.label-terms {
  direction: rtl !important;
}
</style>
