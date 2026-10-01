/**
 * API service layer.
 * All backend communication goes through here.
 */
const API_URL = import.meta.env.VITE_API_URL !== undefined 
  ? import.meta.env.VITE_API_URL 
  : (import.meta.env.DEV ? 'http://localhost:8000' : '')

/**
 * Register a new participant.
 * @param {Object} data - Participant form data
 * @returns {Promise<Object>} - { id, message } on success
 * @throws {Object} - { fieldErrors, message } on failure
 */
export async function registerParticipant(data) {
  try {
    const response = await fetch(`${API_URL}/api/v1/participants/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })

    const result = await response.json()

    if (!response.ok) {
      // DRF returns field-level errors as { field: [errors] }
      const fieldErrors = {}
      let generalMessage = ''

      if (typeof result === 'object' && !Array.isArray(result)) {
        for (const [key, value] of Object.entries(result)) {
          if (key === 'non_field_errors' || key === 'error' || key === 'detail') {
            generalMessage = Array.isArray(value) ? value.join(' ') : value
          } else {
            fieldErrors[key] = Array.isArray(value) ? value.join(' ') : value
          }
        }
      }

      throw {
        fieldErrors,
        message: generalMessage || "Ma'lumotlarni yuborishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.",
        status: response.status,
      }
    }

    return result
  } catch (err) {
    if (err.fieldErrors !== undefined) {
      throw err // Re-throw our structured error
    }
    // Network error
    throw {
      fieldErrors: {},
      message: "Server bilan bog'lanib bo'lmadi. Iltimos, internet aloqangizni tekshiring.",
      status: 0,
    }
  }
}

/**
 * Fetch active event info.
 */
export async function getEventInfo() {
  try {
    const response = await fetch(`${API_URL}/api/v1/event-info/`)
    if (!response.ok) return null
    return await response.json()
  } catch {
    return null
  }
}

/**
 * Fetch certificates/gallery list for the carousel.
 */
export async function getCertificates() {
  try {
    const response = await fetch(`${API_URL}/api/v1/certificates/`)
    if (!response.ok) return []
    return await response.json()
  } catch {
    return []
  }
}

/**
 * Fetch dynamic site media settings (logos, hero and school images).
 */
export async function getSiteSettings() {
  try {
    const response = await fetch(`${API_URL}/api/v1/site-settings/`)
    if (!response.ok) return null
    return await response.json()
  } catch {
    return null
  }
}

/**
 * Fetch list of registered applications/participants with filters.
 */
export async function getApplications(params = {}) {
  try {
    const query = new URLSearchParams()
    if (params.search) query.append('search', params.search)
    if (params.class_number) query.append('class_number', params.class_number)

    const url = `${API_URL}/api/v1/applications/?${query.toString()}`
    const response = await fetch(url)
    if (!response.ok) throw new Error("Ma'lumotlarni yuklab bo'lmadi")
    return await response.json()
  } catch (err) {
    console.error(err)
    return { stats: { total: 0, class_5: 0, class_6: 0, class_7: 0, class_8: 0 }, count: 0, results: [] }
  }
}

/**
 * Delete an application by ID.
 */
export async function deleteApplication(id) {
  try {
    const response = await fetch(`${API_URL}/api/v1/participants/${id}/`, {
      method: 'DELETE',
    })
    return response.ok
  } catch {
    return false
  }
}

/**
 * Get the direct download URL for Excel export.
 */
export function getExportApplicationsUrl(params = {}) {
  const query = new URLSearchParams()
  if (params.search) query.append('search', params.search)
  if (params.class_number) query.append('class_number', params.class_number)
  return `${API_URL}/api/v1/applications/export/?${query.toString()}`
}



