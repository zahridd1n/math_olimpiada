<template>
  <div class="register-page">
    <!-- Subtle Mathematical Curves Background -->
    <div class="math-curves-bg" aria-hidden="true">
      <svg class="math-curves-svg animated-wave-1" viewBox="0 0 1440 900" fill="none">
        <path d="M-100 450 C 300 200, 600 700, 1000 350 C 1250 150, 1400 500, 1600 400" stroke="rgba(229, 178, 46, 0.08)" stroke-width="1.5" />
        <path d="M-50 550 C 350 300, 700 800, 1100 450" stroke="rgba(147, 197, 253, 0.05)" stroke-width="1" />
      </svg>
    </div>

    <div class="container register-container">
      <!-- Form State -->
      <div v-if="!success" class="editorial-card-wrapper">
        <router-link to="/" class="back-link">
          <span class="arrow">←</span> Bosh sahifaga qaytish
        </router-link>

        <div class="form-header">
          <div class="header-kicker">
            <span class="editorial-label">Rasmiy Qabul Shakli</span>
            <span class="editorial-tag">[ 2025/2026 ]</span>
          </div>

          <h1 class="form-title">
            Olimpiadaga <span class="serif-italic-gold">ro'yxatdan</span> <span class="serif-italic">o'tish</span>
          </h1>
          <p class="form-desc">
            Viloyat matematika olimpiadasida ishtirok etish uchun quyidagi ma'lumotlarni to'liq kiriting.
          </p>
        </div>

        <div v-if="serverError" class="error-banner" role="alert">
          {{ serverError }}
        </div>

        <form @submit.prevent="handleSubmit" novalidate class="register-form">
          <!-- Full Name -->
          <div class="form-group" :class="{ error: errors.full_name }">
            <label for="full_name" class="form-label">
              <span>F.I.SH. (O'QUVCHINING TO'LIQ ISMI)</span>
              <span class="required-star">*</span>
            </label>
            <input
              id="full_name"
              v-model="form.full_name"
              type="text"
              class="form-input"
              placeholder="Masalan: Karimov Jasurbek Alisher o'g'li"
              autocomplete="name"
              required
              @blur="validateField('full_name')"
            />
            <span v-if="errors.full_name" class="field-error">{{ errors.full_name }}</span>
          </div>

          <!-- Phone & Birth Date Row -->
          <div class="form-row">
            <div class="form-group" :class="{ error: errors.phone }">
              <label for="phone" class="form-label">
                <span>TELEFON RAQAMI</span>
                <span class="required-star">*</span>
              </label>
              <input
                id="phone"
                v-model="form.phone"
                type="tel"
                class="form-input font-mono"
                placeholder="+998 90 123 45 67"
                autocomplete="tel"
                required
                @blur="validateField('phone')"
                @input="formatPhone"
              />
              <span v-if="errors.phone" class="field-error">{{ errors.phone }}</span>
            </div>

            <div class="form-group" :class="{ error: errors.birth_date }">
              <label for="birth_date" class="form-label">
                <span>TUG'ILGAN SANA</span>
                <span class="required-star">*</span>
              </label>
              <input
                id="birth_date"
                v-model="form.birth_date"
                type="date"
                class="form-input font-mono"
                required
                @blur="validateField('birth_date')"
              />
              <span v-if="errors.birth_date" class="field-error">{{ errors.birth_date }}</span>
            </div>
          </div>

          <!-- Region & District Row -->
          <div class="form-row">
            <div class="form-group" :class="{ error: errors.region }">
              <label for="region" class="form-label">
                <span>VILOYAT</span>
                <span class="required-star">*</span>
              </label>
              <select
                id="region"
                v-model="form.region"
                class="form-input form-select"
                required
                @blur="validateField('region')"
              >
                <option value="" disabled>Viloyatni tanlang</option>
                <option v-for="r in regions" :key="r" :value="r">{{ r }}</option>
              </select>
              <span v-if="errors.region" class="field-error">{{ errors.region }}</span>
            </div>

            <div class="form-group" :class="{ error: errors.district }">
              <label for="district" class="form-label">
                <span>TUMAN YOKI SHAHAR</span>
                <span class="required-star">*</span>
              </label>
              <input
                id="district"
                v-model="form.district"
                type="text"
                class="form-input"
                placeholder="Masalan: Farg'ona shahri"
                required
                @blur="validateField('district')"
              />
              <span v-if="errors.district" class="field-error">{{ errors.district }}</span>
            </div>
          </div>

          <!-- School & Class Row -->
          <div class="form-row">
            <div class="form-group" :class="{ error: errors.school }">
              <label for="school" class="form-label">
                <span>MAKTAB (RAQAMI YOKI NOMI)</span>
                <span class="required-star">*</span>
              </label>
              <input
                id="school"
                v-model="form.school"
                type="text"
                class="form-input"
                placeholder="Masalan: 12-maktab yoki IDUM"
                required
                @blur="validateField('school')"
              />
              <span v-if="errors.school" class="field-error">{{ errors.school }}</span>
            </div>

            <div class="form-group" :class="{ error: errors.class_number }">
              <label for="class_number" class="form-label">
                <span>SINF</span>
                <span class="required-star">*</span>
              </label>
              <select
                id="class_number"
                v-model.number="form.class_number"
                class="form-input form-select font-mono"
                required
                @blur="validateField('class_number')"
              >
                <option value="" disabled>Sinfni tanlang</option>
                <option v-for="c in classOptions" :key="c" :value="c">{{ c }}-sinf</option>
              </select>
              <span v-if="errors.class_number" class="field-error">{{ errors.class_number }}</span>
            </div>
          </div>

          <!-- Teacher Name -->
          <div class="form-group">
            <label for="teacher_name" class="form-label">
              <span>MATEMATIKA O'QITUVCHISI (IXTIYORIY)</span>
            </label>
            <input
              id="teacher_name"
              v-model="form.teacher_name"
              type="text"
              class="form-input"
              placeholder="O'qituvchingiz ism-sharifi"
              autocomplete="off"
            />
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            class="btn-editorial-pill submit-action"
            :disabled="loading"
          >
            <span v-if="loading" class="spinner"></span>
            <span>{{ submitText }}</span>
            <span v-if="!loading">→</span>
          </button>
        </form>
      </div>

      <!-- Success State -->
      <transition name="fade">
        <div v-if="success" class="editorial-card-wrapper success-card">
          <div class="success-badge">[ MUVAFFAQIYATLI RO'YXATDAN O'TILDINGIZ ]</div>
          <h1 class="success-title">
            Tabriklaymiz, siz <span class="serif-italic-gold">qabul qilindingiz!</span>
          </h1>
          <p class="success-text">
            Sizning arizangiz muvaffaqiyatli qabul qilindi. Tez orada koordinatormiz siz bilan bog'lanib, olimpiada yo'riqnomasini taqdim etadi.
          </p>
          
          <div class="success-id-box">
            <span class="editorial-tag">SIZNING ISHTIROKCHI ID RAQAMINGIZ</span>
            <span class="id-value font-mono">#{{ participantId }}</span>
          </div>

          <router-link to="/" class="btn-editorial-pill">
            <span>Bosh sahifaga qaytish</span>
            <span>→</span>
          </router-link>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { registerParticipant } from "../services/api.js"
import { siteConfig } from "../config/site.js"

const route = useRoute()
const router = useRouter()
const regions = siteConfig.regions
const classOptions = [5, 6, 7, 8]

const form = reactive({
  full_name: "",
  phone: "",
  birth_date: "",
  school: "",
  region: "Farg'ona viloyati",
  district: "",
  class_number: "",
  teacher_name: "",
})

const errors = reactive({})
const loading = ref(false)
const success = ref(false)
const serverError = ref("")
const participantId = ref(null)

onMounted(() => {
  if (route.query.phone) {
    form.phone = route.query.phone
    formatPhone()
  }
})

const submitText = computed(() => {
  return loading.value ? "Yuborilmoqda..." : "Ro'yxatdan o'tishni yakunlash"
})

function formatPhone() {
  let v = form.phone.replace(/[^\d+]/g, "")
  if (!v.startsWith("+")) {
    if (v.startsWith("998")) v = "+" + v
    else if (v.startsWith("8") || v.startsWith("9")) v = "+998" + v
  }
  form.phone = v
}

function validateField(field) {
  delete errors[field]
  const v = form[field]

  switch (field) {
    case "full_name":
      if (!v || v.trim().length < 3) errors[field] = "To'liq kiriting"
      break
    case "phone":
      if (!v) { errors[field] = "Kiritish majburiy"; break }
      {
        const cleaned = v.replace(/[^\d+]/g, "")
        if (!/^\+?998\d{9}$/.test(cleaned)) errors[field] = "Noto'g'ri format"
      }
      break
    case "birth_date":
      if (!v) errors[field] = "Kiritish majburiy"
      break
    case "school":
      if (!v || v.trim().length < 2) errors[field] = "Kiritish majburiy"
      break
    case "region":
      if (!v) errors[field] = "Tanlang"
      break
    case "district":
      if (!v || v.trim().length < 2) errors[field] = "Kiritish majburiy"
      break
    case "class_number":
      if (!v) errors[field] = "Tanlang"
      break
  }
  return !errors[field]
}

function validateAll() {
  const fields = ["full_name", "phone", "birth_date", "school", "region", "district", "class_number"]
  let valid = true
  for (const f of fields) {
    if (!validateField(f)) valid = false
  }
  return valid
}

async function handleSubmit() {
  serverError.value = ""
  if (!validateAll()) return
  if (loading.value) return

  loading.value = true

  try {
    const payload = {
      ...form,
      phone: form.phone.replace(/[^\d+]/g, ""),
      class_number: Number(form.class_number),
    }

    const result = await registerParticipant(payload)
    participantId.value = result.id
    success.value = true

    setTimeout(() => {
      router.push("/")
    }, 8000)
  } catch (err) {
    if (err.fieldErrors) {
      for (const [key, msg] of Object.entries(err.fieldErrors)) {
        errors[key] = msg
      }
    }
    serverError.value = err.message || "Xatolik yuz berdi"
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  position: relative;
  background-color: var(--bg-deep);
  padding: calc(var(--header-height) + 40px) 0 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.register-container {
  width: 100%;
  max-width: 680px;
  position: relative;
  z-index: 2;
}

.editorial-card-wrapper {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 16px;
  padding: 48px;
  width: 100%;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-bottom: 28px;
  transition: color 0.2s ease;
}

.back-link:hover {
  color: var(--gold);
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

.form-header {
  margin-bottom: 36px;
}

.form-title {
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 10px;
  line-height: 1.2;
}

.form-desc {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* Error Banner */
.error-banner {
  padding: 14px 18px;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 10px;
  margin-bottom: 24px;
  font-size: 0.88rem;
  color: #fca5a5;
}

/* Register Form */
.register-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 4px;
}

.required-star {
  color: var(--gold);
}

.form-input {
  width: 100%;
  height: 48px;
  padding: 0 16px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-medium);
  border-radius: 10px;
  color: #ffffff;
  font-size: 0.95rem;
  font-family: var(--font-sans);
  transition: all 0.2s ease;
  outline: none;
}

.form-input::placeholder {
  color: var(--text-dim);
  font-size: 0.88rem;
}

.form-input:focus {
  border-color: var(--gold);
  background: rgba(255, 255, 255, 0.05);
  box-shadow: 0 0 16px rgba(229, 178, 46, 0.15);
}

.form-select {
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23e5b22e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  padding-right: 36px;
}

.form-select option {
  background: #0d0a1c;
  color: #ffffff;
}

.form-group.error .form-input {
  border-color: #ef4444;
}

.field-error {
  font-size: 0.75rem;
  color: #f87171;
  font-family: var(--font-sans);
}

.submit-action {
  width: 100%;
  justify-content: center;
  height: 52px;
  font-size: 1rem;
  margin-top: 12px;
}

.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(7, 9, 19, 0.3);
  border-top-color: #070913;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Success Card */
.success-card {
  text-align: center;
  padding: 60px 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.success-badge {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  color: var(--gold);
  margin-bottom: 20px;
}

.success-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 16px;
}

.success-text {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.6;
  max-width: 480px;
  margin-bottom: 32px;
}

.success-id-box {
  background: rgba(229, 178, 46, 0.08);
  border: 1px solid rgba(229, 178, 46, 0.25);
  border-radius: 12px;
  padding: 20px 36px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 36px;
}

.id-value {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--gold);
}

@media (max-width: 768px) {
  .editorial-card-wrapper {
    padding: 32px 20px;
  }
  .form-row {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}
</style>
